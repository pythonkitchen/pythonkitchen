title: How to integrate P5JS with Flask-SocketIO
slug: p5js-with-flask-socket-io
pub: 2022-04-15 20:37:03
authors: arj
tags: 
category: flask

P5Js is an implementation of processing.org's library in JavaSript. It can be thought of as a canvas management library. Integrating such a library with a common backend like Flask unlocks amazing opportunities. Canvas is even better if sockets.io is involved for real-time events. This post shows how to integrate these 3 libraries using flask-socketio.

Main codes
==========


[Github Repo](https://github.com/Abdur-rahmaanJ/p5js-socket-io)

Server:


```python
from shopyo.api.module import ModuleHelp

from flask_socketio import SocketIO, join_room, leave_room, emit

from init import socketio

mhelp = ModuleHelp(__file__, __name__)
globals()[mhelp.blueprint_str] = mhelp.blueprint
module_blueprint = globals()[mhelp.blueprint_str]


@module_blueprint.route("/")
def index():
    return mhelp.render('index.html')


@socketio.on('mouse')# , namespace='/chat')
def mouse(data, methods=['GET', 'POST']):
    # print(data)
    emit('mouse', data, broadcast=True)

```


Client


```python
<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8" />
  <title>Websockets drawing app</title>
  <link rel="stylesheet" type="text/css" href="styles.css" />
  <script src="https://cdn.socket.io/4.4.1/socket.io.min.js" integrity="sha384-fKnu0iswBIqkjxrhQCTZ7qlLHOFEgNkRmK2vaO/LbTZSXdJfAu6ewRBdwHPhBo/H" crossorigin="anonymous"></script>
  <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.3.1/p5.min.js"></script>
  <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.3.1/addons/p5.sound.min.js"></script>
  <script type="text/javascript">


 let socket
let color = '#FFF'
let strokeWidth = 4

function setup() {
  // Creating canvas
  const cv = createCanvas(1000, 1000)
  cv.position(600, 100)
  cv.background(0)

  // Start the socket connection
  socket = io.connect('http://127.0.0.1:5000')

  // Callback function
  socket.on('mouse', data => {
    // console.log('received ' + data.color+ ' '+data.x)
    stroke(data.color)
    strokeWeight(data.strokeWidth)
    line(data.x, data.y, data.px, data.py)
  })

  // Getting our buttons and the holder through the p5.js dom
  const color_picker = select('#pickcolor')
  const color_btn = select('#color-btn')
  const color_holder = select('#color-holder')

  const stroke_width_picker = select('#stroke-width-picker')
  const stroke_btn = select('#stroke-btn')

  // Adding a mousePressed listener to the button
  color_btn.mousePressed(() => {
    // Checking if the input is a valid hex color
    if (/(^#[0-9A-F]{6}$)|(^#[0-9A-F]{3}$)/i.test(color_picker.value())) {
      color = color_picker.value()
      color_holder.style('background-color', color)
    }
    else {console.log('Enter a valid hex value')}
  })

  // Adding a mousePressed listener to the button
  stroke_btn.mousePressed(() => {
    const width = parseInt(stroke_width_picker.value())
    if (width > 0) strokeWidth = width
  })
}

function mouseDragged() {
  // Draw
  stroke(color)
  strokeWeight(strokeWidth)
  line(mouseX, mouseY, pmouseX, pmouseY)

  // Send the mouse coordinates
  sendmouse(mouseX, mouseY, pmouseX, pmouseY)
}

// Sending data to the socket
function sendmouse(x, y, pX, pY) {
  const data = {
    x: x,
    y: y,
    px: pX,
    py: pY,
    color: color,
    strokeWidth: strokeWidth,
  }

  socket.emit('mouse', data)
}
  </script>
  <style type="text/css">
    input.call-picker {
  border: 1px solid #AAA;
  color: #666;
  text-transform: uppercase;
  float: left;
  outline: none;
  padding: 10px;
  text-transform: uppercase;
  width: 85px;
}

.color-picker {
  width: 130px;
  background: #F3F3F3;
  height: 81px;
  padding: 5px;
  border: 5px solid #fff;
  box-shadow: 0px 0px 3px 1px #DDD;
  position: absolute;
  top: 61px;
  left: 2px;
}

.color-holder {
  background: #fff;
  cursor: pointer;
  border: 1px solid #AAA;
  width: 40px;
  height: 36px;
  float: left;
  margin-left: 5px;
}

input.stroke_width_picker {
  border: 1px solid #AAA;
  color: #666;
  text-transform: uppercase;
  float: left;
  outline: none;
  padding: 10px;
  text-transform: uppercase;
  width: 85px;
}

p {
  margin-top: 2rem;
  margin-bottom: 2rem;
}
button {
  margin-left: 1rem;
}
  </style>
</head>

<body>
  <p>Choose color (# hex)</p>
  <input type="text" name="custom_color" placeholder="#FFFFFF" id="pickcolor" class="call-picker" />
  <div id="color-holder" class="color-holder call-picker"></div>
  <button id="color-btn">Change color</button>
  <br />
  <p>Choose stroke width</p>
  <input type="text" name="stroke_width" placeholder="4" id="stroke-width-picker" class="stroke_width_picker" />
  <button id="stroke-btn">Change stroke width</button>
</body>
</html>

```

