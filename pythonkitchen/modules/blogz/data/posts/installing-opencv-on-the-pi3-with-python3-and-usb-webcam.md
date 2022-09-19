title: Installing OpenCv on the Pi3 with python3 (and usb webcam)
slug: installing-opencv-on-the-pi3-with-python3-and-usb-webcam
pub: Wed, 20 Jun 2018 17:59:15 +0000

opencv is one of the most difficult python package to install. it's not a pip install easy package issue. in this post, we'll see how to painlessly install it.
Target Os
=========


we are using noobs [see here](https://www.pythonmembers.club/2018/06/18/raspberry-pi-setup/)
Target Pi
=========


pi3
Existing Instructions
=====================


there are two posts which i found to be nice :

[[pyimagesearch](https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/)] and [[manmade2.com](http://manmade2.com/simple-home-surveillance-with-opencv-3-1-0-on-raspberry-pi-part-1/)]

this tutorial is an explanationless one, refer to these two for explanations
pyimagesearch notes
-------------------


pyimagesearch is the reference post, however, here are some notes:
1. you don't need to expand the filesystem if you are using noobs (the beginner setup)
2. misses qt packages
3. misses python path in ~/.profile
4. uses weird way to modify ~/.profile
5. uses multi-core compiling
6. no working script to test


manmade2.com notes
------------------


1. included wrong make command and reinstall instructions (what if a confused user compiles open cv twice (brr))
2. missed qt packages install
3. misses python path in ~/.profile


Install instructions
====================


the install process can be divided into these parts
1. install raspbian packages including the qt one
2. unzip cv sources
3. setup pip and virtual env
4. compile cv
5. fix rename bug
6. verify installation
7. test snippet


install raspbian packages including the qt one
----------------------------------------------



```python
sudo apt-get update
sudo apt-get upgrade
sudo rpi-update

sudo reboot

sudo apt-get install build-essential git cmake pkg-config
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev

sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev

sudo apt-get install libgtk2.0-dev
sudo apt-get install libatlas-base-dev gfortran

sudo apt-get install python2.7-dev python3-dev

sudo apt install qtbase5-dev
```

unzip cv sources
----------------



```python
cd ~
wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.3.0.zip
unzip opencv.zip

wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.3.0.zip
unzip opencv_contrib.zip
```

setup pip and virtual env
-------------------------



```python
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py

sudo pip install virtualenv virtualenvwrapper
sudo rm -rf ~/.cache/pip
```

**find python path with**

```python
which python
```

**open ~/.profile with**

```python
sudo nano ~/.profile
```

**write at the end**

```python
# virtualenv and virtualenvwrapper
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=/home/pi/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```

**then**

```python
source ~/.profile
```


```python
mkvirtualenv cv -p python3
workon cv
pip install numpy
```

compile cv
----------



```python
workon cv

cd ~/opencv-3.3.0/
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_C_EXAMPLES=OFF \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.3.0/modules \
	-D BUILD_EXAMPLES=ON ..
```


```python
make
```


```python
sudo make install
sudo ldconfig
ls -l /usr/local/lib/python3.5/site-packages/
```

fix rename bug
--------------



```python
cd /usr/local/lib/python3.5/site-packages/

sudo mv cv2.cpython-35m-arm-linux-gnueabihf.so cv2.so

cd ~/.virtualenvs/cv/lib/python3.5/site-packages/

ln -s /usr/local/lib/python3.5/site-packages/cv2.so cv2.so
```

**verify installation**
-----------------------



```python
workon cv
python3
```


```python
>>> import cv2
>>> cv2.__version__
```

should be 3.3.0
test snippet
------------


still inside the environment. create a new test file called cvtest.py

write in it :

```python
import cv2
import time

class CameraInst():
        # Constructor...
        def __init__(self):
                fps        = 20.0               # Frames per second...
                resolution = (640, 480)         # Frame size/resolution...
                w = 640
                h = 480

                self.cap = cv2.VideoCapture(0)  # Capture Video...
                print("Camera warming up ...")
                time.sleep(1)

                # Define the codec and create VideoWriter object
                fourcc = cv2.VideoWriter_fourcc(*"H264")     # You also can use (*'XVID')
                self.out = cv2.VideoWriter('output.avi',fourcc, fps, (w, h))

        def captureVideo(self):
                # Capture
                self.ret, self.frame = self.cap.read()
                # Image manipulations come here...
                self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
                cv2.imshow('frame',self.gray)

        def saveVideo(self):
                # Write the frame
                self.out.write(self.frame)

        def __del__(self):
                self.cap.release()
                cv2.destroyAllWindows()
                print("Camera disabled and all output windows closed...")

def main():
        cam1 = CameraInst()

        while(True):
                # Display the resulting frames...
                cam1.captureVideo()    # Live stream of video on screen...
                cam1.saveVideo()       # Save video to file 'output.avi'...
                if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

        cleanUp()

if __name__=='__main__':
        main()
```

run with

```python
python3 cvtest.py
```

i tetsted it with a usb webcam
Further notes
-------------


if you are following pyimage search, changing swap size then /etc/dphys-swapfile is a file without extentions, not  a directory

if you are getting function not implemented don't forget sudo apt install qtbase5-dev

if you can't open ~/.profile with nano, make sure you put sudo before i.e. sudo nano ~/.profile 

if you are getting

> virtualenvwrapper.sh: There was a problem running the initialization hooks.



> If Python could not import the module virtualenvwrapper.hook\_loader,
> check that virtualenvwrapper has been installed for
> VIRTUALENVWRAPPER\_PYTHON=/usr/bin/python and that PATH is
> set properly.


make sure you set the python path as above (the which python part)

 

 

 
