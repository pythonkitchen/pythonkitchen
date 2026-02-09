title: Remote Access: How to Establish an SSH Connection to Your Raspberry Pi
slug: raspberry-pi-setup-establishing-ssh-connection
pub: 2018-06-20 16:44:45
authors: arj
tags: raspberry-pi, ssh, linux, remote-access, networking
category: raspberry pi

One of the greatest features of the Raspberry Pi is that you don't actually need a dedicated monitor or keyboard to use it. Through **SSH (Secure Shell)**, you can control your Pi's terminal from your main laptop, tablet, or even your smartphone. 

This is known as running "headless," and it is the standard way to manage Raspberry Pi servers and IoT projects.

---

## Prerequisites

Before you can connect, ensure that:
1.  **SSH is enabled on the Pi:** You can do this via the "Interfacing Options" in `sudo raspi-config` or by placing an empty file named `ssh` in the root of your SD card.
2.  **Both devices are on the same network:** Your computer and the Pi must be connected to the same Wi-Fi or Ethernet router.

---

## Step 1: Find Your Pi's IP Address

To connect, you need to know where the Pi is on your network.

### Method A: Use the Hostname
By default, the Pi's hostname is `raspberrypi`. Most modern routers and computers allow you to reach it at `raspberrypi.local`.

### Method B: Network Scanning
If the hostname doesn't work, you can scan your network for devices.
*   **Mobile:** Use an app like **Fing** or **FindPi** to see a list of all devices on your Wi-Fi.
*   **Desktop:** Use **Angry IP Scanner** to find the IP address (usually looks like `192.168.1.X`).

---

## Step 2: Connecting via SSH

### On Windows (using PuTTY)
1.  Download and open [PuTTY](https://www.putty.org/).
2.  In the **Host Name** field, enter the IP address or `raspberrypi.local`.
3.  Ensure the port is set to **22**.
4.  Click **Open**. If a security alert appears, click "Yes."

### On macOS / Linux (using Terminal)
Open your terminal and type the following command:
```bash
ssh pi@raspberrypi.local
```
*(Replace `raspberrypi.local` with the IP address if needed)*

---

## Step 3: Logging In

When prompted, enter the default credentials:
*   **Default Username:** `pi`
*   **Default Password:** `raspberry`

*Note: When you type your password, you won't see any characters appearing on the screen. This is a security feature in Linux—just type it blindly and hit Enter.*

---

## Essential Security: Change Your Password!

Now that you are logged in, the first thing you should do is change the default password. Since every Pi starts with the same password, leaving it unchanged makes your device a target for hackers.

Type this command and follow the prompts:
```bash
passwd
```

## Conclusion

You are now controlling your Raspberry Pi remotely! You can run updates, install software, and write code all from the comfort of your main computer. SSH is an essential skill for any Pi enthusiast.

### Next Steps:
*   [How to Install OpenCV on your Pi 3](https://www.pythonkitchen.com/installing-opencv-on-the-pi3-with-python3-and-usb-webcam/)
*   [Building a Web Mail Interface with Flask and Pi](https://www.pythonkitchen.com/web-mail-interface-using-pi-and-flask/)