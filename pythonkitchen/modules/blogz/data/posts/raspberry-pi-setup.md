title: Raspberry-Pi setup - part 1 : OS installation
slug: raspberry-pi-setup
pub: Mon, 18 Jun 2018 11:42:03 +0000

In this post we'll cover the software setup part. The raspberry pi is an empty computer, empty of peripherals and os. the first step is to install the os.
Target Model
============


raspberry pi 3

![](https://www.raspberrypi.org/app/uploads/2017/05/Raspberry-Pi-3-462x322.jpg)
Needed
======


* sd card at least 8gb
* hdmi cable
* monitor
* charger
* usb mouse
* usb keyboard


only power and hdmi cable + monitor needed if testing if installation ok. tv passes as monitor
Installing the OS
=================


the steps are outlined as follows ;
* format sd card
* download the os pack
* extract to sd card
* add empty ssh file (optional)


format sd card
--------------


download the sdcard association's formatter [[windows](https://www.sdcard.org/downloads/formatter_4/eula_windows/index.html)]

insert the sd card on your pc (the sd card is in the holder, you insert the holder on your pc)

use the formatter to format the sdcard to FAT32
download the os pack
--------------------


download NOOBS from [[here](https://www.raspberrypi.org/downloads/)]

NOOBS stands for New Out Of the Box Software. It is an installer with many programs included, including raspbian, the linux flavoured distribution.

extract the zip file to the formatted sdcard (choose the sdcard location)
add empty ssh file (optional)
-----------------------------


create an empty ssh file (filename : ssh, no extention) in the sdcard (root directory). this will enable ssh by default.

ssh can also be enabled by gui after boot
Booting
=======


insert the sd card in the pi at the sd card slot at the bottom, plug the hdmi cable to your monitor and pi and  power on.

you should see some installation instruction

choose raspbian and click the install tab/button above.

that's it !

 

 

 
