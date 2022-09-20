title: How to Integrate Tinymce 5 with Flask (with csrf)
slug: integrate-tinymce-5-with-flask
pub: Thu, 09 Dec 2021 07:32:00 +0000
authors: Abdur-RahmaanJ

This article shows how to integrate Tinymce 5 with Flask even including csrf protection!

Text area


```python
<textarea id="content"></textarea>

```


Tinymce


```python
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/tinymce/5.10.2/tinymce.min.js"></script>
<script type="text/javascript">
tinymce.init({
    selector: '#content',
    plugins: [
        'advlist autolink link image imagetools lists charmap print preview hr anchor pagebreak spellchecker',
        'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
        'save table contextmenu directionality template paste textcolor codesample'
    ],
    imagetools_toolbar: "rotateleft rotateright | flipv fliph | editimage imageoptions",
    toolbar: 'insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | print preview media fullpage | forecolor backcolor emoticons | codesample',
    relative_urls: false,
    images_upload_handler : function(blobInfo, success, failure) {
            var xhr, formData;

            xhr = new XMLHttpRequest();
            xhr.withCredentials = false;
            xhr.open('POST', '{{ url_for('upload_function_name_here') }}'); // change this

            xhr.onload = function() {
                var json;

                if (xhr.status != 200) {
                    failure('HTTP Error: ' + xhr.status);
                    return;
                }

                json = JSON.parse(xhr.responseText);

                // if (!json || typeof json.file_path != 'string') {
                //     failure('Invalid JSON: ' + xhr.responseText);
                //     return;
                // }

                success(json.location);
            };

            formData = new FormData();
            formData.append('file', blobInfo.blob(), blobInfo.filename());
            formData.append('csrf_token', '{{csrf_token()}}'); // i add csrf_token

            xhr.send(formData);
        },
    image_title: true,
    automatic_uploads: true,
    images_reuse_filename: false,
    images_upload_base_path: '/static/gallery/', // i serve from /static/gallery and save to /static/gallery
    codesample_languages: [
        { text: 'HTML/XML', value: 'markup' },
        { text: 'JavaScript', value: 'javascript' },
        { text: 'CSS', value: 'css' },
        { text: 'Processing', value: 'processing' },
        { text: 'Python', value: 'python' }
    ],
    width: "100%",
});
</script>

```


First add to config GALLERY\_UPLOAD\_PATH with value the absolute path of your static folder

flask


```python
from flask import abort
from flask import current_app
from flask import Response
from flask import request
from flask import url_for
from flask import jsonify

from werkzeug.utils import secure_filename

@module_blueprint.route('/file-upload', methods=['GET', 'POST'])
def file_upload():
    """
    Upload post images from tinyMce editor.
    Save image to path.
    returns: json { location: path }
    """

    # Get the file user has uploaded inside the tinymce editor.
    uploaded_file = request.files.get('file')

    if uploaded_file:
        filename = secure_filename(uploaded_file.filename).lower()

        # Validate the contents of the file.  Check the header of the file is infact an image.
        # valid_img_ext = validate_img(uploaded_file.stream)

        # Split filename and extension, rename & add correct extension.
        # filename = secure_filename(os.path.splitext(filename)[0] + valid_img_ext)

        img_path = os.path.join(current_app.config['GALLERY_UPLOAD_PATH'], filename)

        # Check if user directory exists, create if nessecary.
        if not os.path.exists(current_app.config['GALLERY_UPLOAD_PATH']):
            try:
                os.makedirs(current_app.config['GALLERY_UPLOAD_PATH'])
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        # Save the image.
        uploaded_file.save(img_path)
        location = url_for('static', filename='gallery/' + filename)
        print(location)

        # Return image path back to editor
        return jsonify({'location': location})

    abort(Response('404 - Image failed to upload'))

```


Flask 2.x

[Kevin7's](https://www.kevin7.net/post_detail/tinymce-and-flask) article was not working, adapted it
