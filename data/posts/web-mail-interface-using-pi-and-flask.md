title: Building a Web Mail Client with Flask and Raspberry Pi
slug: web-mail-interface-using-pi-and-flask
pub: 2018-07-01 07:32:45
authors: arj
tags: python, flask, raspberry-pi, smtplib, web-development
category: raspberry pi

Have you ever wondered how web-based email clients like Gmail or Outlook actually work? At their core, they are web applications that take user input and send it to an email server. In this tutorial, we will build a basic web mail interface using **Flask** and a **Raspberry Pi**.

By the end of this guide, you’ll have a local web server running on your Pi that allows any device on your network to send emails.

---

## 1. Flask Basics: Setting Up the Project

Flask is a "micro" web framework for Python. It’s lightweight and easy to learn, making it perfect for Raspberry Pi projects.

### Project Structure
Create a folder for your project and organize it like this:
```text
sendmail/
├── app.py           # Your Python logic
├── templates/       # HTML files
│   └── index.html
└── static/          # CSS, JS, and Images
    └── style.css
```

---

## 2. Creating the Email Interface (HTML)

We need a simple form where users can enter the recipient, the subject, and the message body. Save this as `templates/index.html`.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Pi Mailer</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: sans-serif; padding: 20px; max-width: 500px; margin: auto; }
        input, textarea { width: 100%; margin-bottom: 10px; padding: 8px; }
        input[type="submit"] { background: #4f46e5; color: white; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <h2>Send Email via Pi</h2>
    <form method="POST">
        <label>To:</label>
        <input type="email" name="to" required>
        
        <label>Subject:</label>
        <input type="text" name="subject" required>
        
        <label>Body:</label>
        <textarea name="body" rows="5" required></textarea>
        
        <input type="submit" value="Send Email">
    </form> 
</body>
</html>
```

---

## 3. The Backend: Sending Mail with `smtplib`

Python’s built-in `smtplib` library allows us to connect to an SMTP server (like Gmail) to send messages.

### A Note on Security
**Important:** Do not use your primary Gmail password in your code. Most modern providers require you to generate an **"App Password"** specifically for your script. This keeps your main account secure.

### The Python Script (`app.py`)

```python
from flask import Flask, render_template, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

def send_mail(to_email, subject, message_body):
    # Configuration
    MY_EMAIL = "your-email@gmail.com"
    MY_PASSWORD = "your-app-password" # Use an App Password here!
    
    # Setup the MIME
    msg = MIMEMultipart()
    msg['From'] = MY_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message_body, 'plain'))
    
    # Connect to Gmail's SMTP server
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() # Secure the connection
        server.login(MY_EMAIL, MY_PASSWORD)
        server.send_mail(MY_EMAIL, to_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        to = request.form['to']
        subject = request.form['subject']
        body = request.form['body']
        
        if send_mail(to, subject, body):
            return f"<h3>Success! Mail sent to {to}</h3> <a href='/'>Send another</a>"
        else:
            return "<h3>Failed to send mail. Check console for errors.</h3>"
            
    return render_template('index.html')

if __name__ == '__main__':
    # host='0.0.0.0' allows access from other devices on the network
    app.run(debug=True, host='0.0.0.0', port=5000)
```

---

## 4. Running the App on Your Pi

1.  Open your Pi’s terminal and navigate to the `sendmail` folder.
2.  Run the app: `python app.py`
3.  On your Pi, you can access it at `http://localhost:5000`.
4.  On any other device on the same Wi-Fi, find your Pi's IP address (e.g., `192.168.1.15`) and visit `http://192.168.1.15:5000`.

## Conclusion

You’ve just built a functional IoT device! This project combines web development, networking, and the Python standard library into a practical tool. From here, you could add an "attachments" feature or even a simple database to keep track of sent emails.

### Related Posts:
*   [Setting up SSH for Headless Raspberry Pi access](https://www.pythonkitchen.com/raspberry-pi-setup-establishing-ssh-connection/)
*   [How to install OpenCV on your Pi](https://www.pythonkitchen.com/installing-opencv-on-the-pi3-with-python3-and-usb-webcam/)