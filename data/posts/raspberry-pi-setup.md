title: Setting Up Your Raspberry Pi 3: A Step-by-Step OS Installation Guide
slug: raspberry-pi-setup
pub: 2018-06-18 11:42:03
authors: arj
tags: raspberry-pi, hardware, linux, tutorial, beginners
category: raspberry pi

The Raspberry Pi is a remarkably powerful credit-card-sized computer, but when you first take it out of the box, it’s a "blank slate." It has no operating system and no built-in storage. In this first part of our setup series, we’ll cover how to install the OS and get your Pi up and running.

## Hardware Requirements

To get started with a Raspberry Pi 3, you will need:
*   **MicroSD Card:** At least 8GB (Class 10 is recommended for speed).
*   **Power Supply:** A 5V 2.5A Micro USB power adapter.
*   **HDMI Cable & Monitor:** To see what's happening.
*   **USB Mouse & Keyboard:** For initial configuration.
*   **Internet Connection:** Either an Ethernet cable or Wi-Fi.

---

## Step 1: Choosing Your Operating System

While there are many OS options (Ubuntu, RetroPie, etc.), **Raspberry Pi OS** (formerly known as Raspbian) is the official and most stable choice for beginners.

### The Modern Way: Raspberry Pi Imager
Back in the day, we used a tool called NOOBS. Today, the easiest method is using the **Raspberry Pi Imager**, which you can download for Windows, macOS, or Linux from the [official website](https://www.raspberrypi.com/software/).

---

## Step 2: Flashing the SD Card

1.  Insert your MicroSD card into your computer.
2.  Open the **Raspberry Pi Imager**.
3.  Click **CHOOSE OS** and select "Raspberry Pi OS (32-bit)".
4.  Click **CHOOSE STORAGE** and select your SD card.
5.  *(Optional but Recommended)* Click the **Gear Icon** (Advanced Options) to pre-configure your Wi-Fi, set a hostname (like `pi.local`), and enable SSH.
6.  Click **WRITE** and wait for the process to finish.

---

## Step 3: First Boot

1.  Insert the MicroSD card into the slot on the underside of your Raspberry Pi.
2.  Connect your monitor via HDMI and plug in your mouse and keyboard.
3.  **Finally, plug in the power cable.** The Pi doesn't have a power button; it turns on as soon as it gets power.

You should see a splash screen followed by the desktop. Follow the on-screen setup wizard to set your location, change your password, and check for software updates.

## Enabling SSH (Headless Setup)

If you don't have a spare monitor, you can run the Pi "headless." To do this, create an empty file named `ssh` (no file extension) in the root directory of the SD card after flashing it. This tells the Pi to enable Remote Terminal access as soon as it boots.

## Conclusion

Congratulations! You now have a working Linux computer the size of a deck of cards. In the next part of this series, we’ll look at how to **connect to your Pi remotely via SSH** so you can control it from your main laptop.

### Next Steps:
*   [Establishing an SSH Connection to your Pi](https://www.pythonkitchen.com/raspberry-pi-setup-establishing-ssh-connection/)
*   [Installing OpenCV for Computer Vision Projects](https://www.pythonkitchen.com/installing-opencv-on-the-pi3-with-python3-and-usb-webcam/)