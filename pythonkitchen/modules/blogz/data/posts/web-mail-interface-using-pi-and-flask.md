title: web mail interface using pi and flask
slug: web-mail-interface-using-pi-and-flask
pub: Sun, 01 Jul 2018 07:32:45 +0000
authors: Abdur-RahmaanJ

have you ever used gmail or hotmail on the web? it seems so natural that we take it for granted. in this post we'll see how to build a basic web mail client to send mail ... using flask and pi as server. this is
content
=======


flask intro : folder structure

flask intro : requests

flask : basic app

flask : post
flask intro : folder structure
==============================


flask is a python web framework, it is recommended to learn it before django. a typical flask project structure is as follows:

let us say we name our project sendmail, the project structure is

```python
sendmail [folder]
|_ _ app.py
|_ _ templates [folder]
|     |_ _ file.html
|_ _ static [folder]
      |_ _ style.css
```

to run a flask app you don't need the templates and static folder but they are here for good reasons
the templates folder
--------------------


let us say you have a website and for each page there are some elements recurring like the header and footer. having a template allows you to specify only the changing data
templating engine
-----------------


flask uses the [jinja](http://jinja.pocoo.org/docs/2.10/) templating engine for rendering variables etc

{{name}} will display the variable name on rendering. more on that later
static folder
-------------


static means it won't change, load your non-changing assets in there
flask intro : requests
======================


for a webserver, whatever you type in the address bar after specifying the correct ip is a request

```python
http://www.domain.com/water.html
```

requests the file water.html

in flask however (and python), you need not request for only files, you can pretty much mould the request pattern

```python
http://www.domain.com/mult/5/by/2

http://www.domain.com/show/user54/sea
```

flask : basic app
=================


a basic app in flask is as follows :

```python
from flask import Flask

app = Flask(__name__)
@app.route('/')
def basic():
    return 'welcome to my site'
if __name__ == '__main__': # if file run
    app.run(debug=True, host='0.0.0.0')
```

explanations

```python
@app.route('/')
```

means the first slash after the domain name if requested

you define the action in the subsequent function, which can be named as you want

let us say the domain is www.d.com, we are specifying what to do when www.d.com/ is requested

```python
return 'welcome to my site'
```

displays a single string

```python
app.run(debug=True, host='0.0.0.0')
```

host='0.0.0.0' runs the app on 192.168. ...
flask : basic app : return page
===============================



```python
from flask import Flask, render_tempplate

app = Flask(__name__)
@app.route('/')
def basic():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

```

here

```python
return render_template('index.html')
```

returns the file index.html in the templates folder
flask : post
============


there are two request methods viz post and get, post is more secure than get

here is a post demo :

our html

```python
<form method="POST">
<input type="text" name="xyz">
<br>
<input type="submit" value="Send">
</form>
```

our post handling method:

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST': #this block is only entered when the form is submitted
        data = request.form['xyz']
        return 'data entered :{}'.format(data)
    
    return render_template('index.html')

```

our app
=======


here is the code for our index.html file in our templates folder :

```python
<!DOCTYPE html>
<html>
<head>
<title></title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<form method="POST">
to:<br>
<input type="text" name="to">
<br>
subject:<br>
<input type="text" name="subject">
<br>
body:<br>
<textarea rows="4" cols="50" type="text" name="body">

</textarea>
<br><br>
<input type="submit" value="Send">
</form> 
</body>
</html>
```

our app.py code :
-----------------



```python
from flask import Flask, render_template, request

# send mail function
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

def send_mail(to_, subject_, body_):
    fromaddr='[address]'
    toaddr=to_
    thesub=subject_
    thebody=body_
    thepassword='[pass]'
    domsmtp='smtp.gmail.com'
    smtpport= 587 #needs integer not string

     
    msg = MIMEMultipart('alt text here')
    msg.set_charset('utf8')

     
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = Header(thesub,'utf8')
    _attach = MIMEText(thebody.encode('utf8'),'html','UTF-8')
    msg.attach(_attach)
                       
    server = smtplib.SMTP(domsmtp, smtpport)
    server.starttls()
    server.login(fromaddr, thepassword)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)

    server.quit()
    print('mail sent')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST': #this block is only entered when the form is submitted
        to = request.form['to']
        subject = request.form['subject']
        body = request.form['body']
        send_mail(to, subject, body)
        return 'mail sent to {}'.format(to)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```

just replace [address] and [pass] by your actual data
now run app.py, and see the output

you can grab another device on the network, go to 192.168. ... depending, and ... you can send a mail from another device, from a web interface
