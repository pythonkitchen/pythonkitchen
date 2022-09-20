title: How to get server response from DropzoneJs for chunk uploads
slug: dropzonejs-server-response-chunck-upload
pub: Fri, 13 Aug 2021 08:47:49 +0000
authors: Abdur-RahmaanJ

After much struggling, here's the magical formula we got for getting the server response back for chunck uploads:


```python
var myDropzone = new Dropzone(document.body, { // Make the whole body a dropzone
    thumbnailWidth: 80,
    thumbnailHeight: 80,
    parallelUploads: 20,
    previewTemplate: previewTemplate,
    autoQueue: false, // Make sure the files aren't queued until manually added
    previewsContainer: "#previews", // Define the container to display the previews
    clickable: ".fileinput-button", // Define the element that should be used as click trigger to select files.
    paramName: 'file',
    chunking: true,
    forceChunking: true,
    url: upload_url,
    maxFilesize: 1025, // megabytes
    chunkSize: 1000000, // bytes
    init: function () {
        this.on("complete", function (file){
          console.log(file.xhr.response);
        });
    }


})

```

