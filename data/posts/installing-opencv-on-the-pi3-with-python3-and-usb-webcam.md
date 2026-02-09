title: The Ultimate Guide to Installing OpenCV on Raspberry Pi 3
slug: installing-opencv-on-the-pi3-with-python3-and-usb-webcam
pub: 2018-06-20 17:59:15
authors: arj
tags: python, opencv, raspberry-pi, computer-vision, tutorial
category: computer vision, raspberry pi

OpenCV (Open Source Computer Vision Library) is the industry standard for image processing and computer vision. However, installing it on a Raspberry Pi 3 can be notoriously difficult. While modern versions of Python allow for a simple `pip install opencv-python`, compiling it from source is still often the best way to get full hardware optimization and support for extra modules.

In this guide, we provide a streamlined, "painless" workflow for installing OpenCV 3.3.0 with Python 3 support on your Pi.

---

## Step 1: Install Dependencies

Before we touch OpenCV, we need to install the various libraries and tools that it relies on for handling images, videos, and graphical windows.

```bash
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install build-essential git cmake pkg-config -y
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev -y
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y
sudo apt-get install libxvidcore-dev libx264-dev -y
sudo apt-get install libgtk2.0-dev libatlas-base-dev gfortran -y
sudo apt-get install python2.7-dev python3-dev qtbase5-dev -y
```

---

## Step 2: Download OpenCV Source Code

We need both the main OpenCV repository and the "contrib" repository, which contains experimental features.

```bash
cd ~
wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.3.0.zip
unzip opencv.zip

wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.3.0.zip
unzip opencv_contrib.zip
```

---

## Step 3: Set Up a Virtual Environment

It is highly recommended to install OpenCV inside a virtual environment to keep your global Python installation clean.

```bash
sudo pip install virtualenv virtualenvwrapper
source ~/.profile

# Create the environment
mkvirtualenv cv -p python3
workon cv
pip install numpy
```

---

## Step 4: Compiling OpenCV (The Long Part)

This is where the actual building happens. This process can take 1 to 2 hours depending on your SD card speed.

```bash
cd ~/opencv-3.3.0/
mkdir build && cd build

cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_C_EXAMPLES=OFF \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.3.0/modules \
	-D BUILD_EXAMPLES=ON ..

# Start the compilation (use all 4 cores of the Pi 3)
make -j4
sudo make install
sudo ldconfig
```

---

## Step 5: Verification

To ensure everything worked, activate your environment and try to import the library in Python:

```python
workon cv
python
>>> import cv2
>>> print(cv2.__version__)
'3.3.0'
```

---

## Bonus: Testing with a USB Webcam

Once installed, use this quick script to verify that OpenCV can capture video from a standard USB webcam.

```python
import cv2

# 0 is usually the index for the first USB camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    # Convert to grayscale for a classic CV look
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('OpenCV Test', gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

## Conclusion

Installing OpenCV from source on a Raspberry Pi is a badge of honor for any computer vision enthusiast. You now have a high-performance environment ready for facial recognition, object tracking, and much more!

### Next Steps:
*   [Setting up an SSH connection for remote coding](https://www.pythonkitchen.com/raspberry-pi-setup-establishing-ssh-connection/)
*   [Building a Smart Home Hub with Raspberry Pi](https://www.pythonkitchen.com/raspberry-pi-setup/)