"""
Temporary notice:

Need help?

- Join the discord https://discord.com/invite/k37Ef6w
- Raise an issue https://github.com/shopyo/shopyo/issues/new/choose
- Mail maintainers https://github.com/shopyo/shopyo#-contact

Hope it helps! We welcome all questions and even requests for walkthroughs
"""
import importlib
import os
import pkgutil
import sys
import markdown
import datetime
import click
import jinja2
from flask import Flask
from flask_admin import Admin
from flask_admin.menu import MenuLink
from flask_login import current_user

from shopyo.api.assets import register_devstatic
from shopyo.api.file import trycopy


base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, base_path)
from config import app_config
from init import csrf


from init import load_extensions
from init import modules_path
from init import installed_packages



from shopyo_admin import DefaultModelView
from shopyo_admin import MyAdminIndexView


def create_app(config_name="development"):

    global_template_variables = {}
    global_configs = {}
    app = Flask(
        __name__,
        instance_path=os.path.join(base_path, "instance"),
        instance_relative_config=True,
    )

    load_plugins(app, global_template_variables, global_configs, config_name)
    load_config_from_obj(app, config_name)
    load_config_from_instance(app, config_name)
    create_config_json()
    load_extensions(app)
    setup_flask_admin(app)
    register_devstatic(app, modules_path)
    load_blueprints(app, config_name, global_template_variables, global_configs)
    setup_theme_paths(app)
    inject_global_vars(app, global_template_variables)


    @app.cli.command("upload-posts")
    def upload_posts():
        from modules.blogz.models import Blog
        from modules.box__default.auth.models import User
        from init import db
        user = User.query.filter(User.email == 'admin@domain.com').first()

        with app.app_context():
            for file in os.listdir('./modules/blogz/data/posts'):
                with open(f'./modules/blogz/data/posts/{file}') as f:
                    
                    l = f.read().split('\n\n')
                    content = '\n\n'.join(l[1:])

                    meta = l[0].split('\n')
                    metadata = {}
                    for line in meta:
                        metadata[line.split(':')[0].strip()] = ''.join(line.split(':')[1:]).strip()

                    # print(metadata['pub'])
                    # Wed, 24 Feb 2021 094049 +0000

                    month_map = {'jan':1, 'feb':2, 'mar':3,
                    'apr':4, 'may':5, 'jun':6, 'jul':7, 'aug':8, 'sep':9,
                    'oct':10, 'nov':11, 'dec':12}
                    year = int(metadata['pub'].split()[3])

                    raw_month = metadata['pub'].split()[2]
                    month = int(month_map[raw_month.casefold()])
                    day = int(metadata['pub'].split()[1])

                    time_raw = metadata['pub'].split()[4]

                    hour = int(time_raw[0]+time_raw[1])
                    minute = int(time_raw[2]+time_raw[3])
                    second = int(time_raw[4]+time_raw[5])

                    # print(year, month, day, hour, minute, second)
                    pub = datetime.datetime(year, month, day, hour, minute, second) 

                    slug = metadata['slug']
                    if metadata['slug'].startswith('?p='):
                        continue

                    post_exists = Blog.query.filter(Blog.slug==slug).first()
                    if post_exists:
                        continue
                    bpost = Blog(title=metadata['title'],
                        source=content, slug=metadata['slug'], pub=pub)
                    bpost.authors.append(user)
                    db.session.add(bpost)
            db.session.commit()
                
    return app


def load_plugins(app, global_template_variables, global_configs, config_name):
    for plugin in installed_packages:
        if plugin not in ["shopyo_admin"]:
            try:
                mod = importlib.import_module(f"{plugin}.view")
                app.register_blueprint(getattr(mod, f"{plugin}_blueprint"))
            except AttributeError:
                # print("[ ] Blueprint skipped:", e)
                pass

            # global's available everywhere template vars
            try:
                mod_global = importlib.import_module(f"{plugin}.global")
                global_template_variables.update(mod_global.available_everywhere)
            except ImportError:
                # print(f"[ ] {e}")
                pass

            except AttributeError:
                pass

            # load configs
            try:
                mod_global = importlib.import_module(f"{plugin}.global")
                if config_name in mod_global.configs:
                    global_configs.update(mod_global.configs.get(config_name))
            except ImportError:
                # print(f"[ ] {e}")
                pass
            except AttributeError:
                # click.echo('info: config not found in global')
                pass


def load_config_from_obj(app, config_name):

    try:
        configuration = app_config[config_name]
    except KeyError as e:
        print(
            f"[ ] Invalid config name {e}. Available configurations are: "
            f"{list(app_config.keys())}\n"
        )
        sys.exit(1)

    app.config.from_object(configuration)


def load_config_from_instance(app, config_name):

    if config_name != "testing":
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)

    # create empty instance folder and empty config if not present
    try:
        os.makedirs(app.instance_path)
        with open(os.path.join(app.instance_path, "config.py"), "a"):
            pass
    except OSError:
        pass


def create_config_json():
    if not os.path.exists("config.json"):
        trycopy("config_demo.json", "config.json")


def setup_flask_admin(app):
    from init import db
    from modules.box__default.auth.models import User
    from modules.blogz.models import Blog

    admin = Admin(
        app,
        name="My App",
        template_mode="bootstrap4",
        index_view=MyAdminIndexView(),
    )
    admin.add_view(DefaultModelView(Blog, db.session))
    admin.add_view(DefaultModelView(User, db.session))
    admin.add_link(MenuLink(name="Logout", category="", url="/auth/logout?next=/admin"))


def load_blueprints(app, config_name, global_template_variables, global_configs):
    """
    - Registers blueprints
    - Adds global template objects from modules
    - Adds global configs from modules
    """

    for folder in os.listdir(os.path.join(base_path, "modules")):
        if folder.startswith("__"):  # ignore __pycache__
            continue

        if folder.startswith("box__"):
            # boxes
            for sub_folder in os.listdir(os.path.join(base_path, "modules", folder)):
                if sub_folder.startswith("__"):  # ignore __pycache__
                    continue
                elif sub_folder.endswith(".json"):  # box_info.json
                    continue
                try:
                    sys_mod = importlib.import_module(
                        f"modules.{folder}.{sub_folder}.view"
                    )
                    app.register_blueprint(getattr(sys_mod, f"{sub_folder}_blueprint"))
                except AttributeError:
                    pass
                try:
                    mod_global = importlib.import_module(
                        f"modules.{folder}.{sub_folder}.global"
                    )
                    global_template_variables.update(mod_global.available_everywhere)
                except ImportError:
                    pass

                except AttributeError:
                    pass

                # load configs
                try:
                    mod_global = importlib.import_module(
                        f"modules.{folder}.{sub_folder}.global"
                    )
                    if config_name in mod_global.configs:
                        global_configs.update(mod_global.configs.get(config_name))
                except ImportError:
                    pass

                except AttributeError:
                    # click.echo('info: config not found in global')
                    pass
        else:
            # apps
            try:
                mod = importlib.import_module(f"modules.{folder}.view")
                app.register_blueprint(getattr(mod, f"{folder}_blueprint"))
            except AttributeError:
                # print("[ ] Blueprint skipped:", e)
                pass

            # global's available everywhere template vars
            try:
                mod_global = importlib.import_module(f"modules.{folder}.global")
                global_template_variables.update(mod_global.available_everywhere)
            except ImportError:
                # print(f"[ ] {e}")
                pass

            except AttributeError:
                pass

            # load configs
            try:
                mod_global = importlib.import_module(f"modules.{folder}.global")
                if config_name in mod_global.configs:
                    global_configs.update(mod_global.configs.get(config_name))
            except ImportError:
                # print(f"[ ] {e}")
                pass
            except AttributeError:
                # click.echo('info: config not found in global')
                pass

    app.config.update(**global_configs)


def setup_theme_paths(app):
    with app.app_context():
        front_theme_dir = os.path.join(
            app.config["BASE_DIR"], "static", "themes", "front"
        )
        back_theme_dir = os.path.join(
            app.config["BASE_DIR"], "static", "themes", "back"
        )

        if os.path.exists(front_theme_dir) and os.path.exists(back_theme_dir):
            my_loader = jinja2.ChoiceLoader(
                [
                    app.jinja_loader,
                    jinja2.FileSystemLoader([front_theme_dir, back_theme_dir]),
                ]
            )
            app.jinja_loader = my_loader


def inject_global_vars(app, global_template_variables):
    @app.context_processor
    def inject_global_vars():
        APP_NAME = "dwdwefw"

        base_context = {
            "APP_NAME": APP_NAME,
            "len": len,
            "current_user": current_user,
        }
        base_context.update(global_template_variables)

        return base_context
