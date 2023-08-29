title: Raspberry-Pi setup – part 2 : establishing ssh connection
slug: raspberry-pi-setup-establishing-ssh-connection
pub: 2018-06-20 16:44:45
authors: arj
tags: 
category: raspberry pi

establishing an ssh connection is incredibly useful to manage your pi from another device/remotely be it your android phone or pc

![](https://www.putty.org/Putty.png)
Steps
=====


* connect the pi to the internet
* locate pi
* start ssh connection


connect the pi to the internet
------------------------------


using a two endpoints network cable, connect the pi to your router, or if you have a monitor+keyboard+mouse setup, connect to wifi (we are using pi3)
Locating the pi
---------------


(make sure [ssh is enabled](https://www.pythonmembers.club/2018/06/18/raspberry-pi-setup/) before)

you can use [angry scanner](https://angryip.org/download/) in the range 192.168.137.0 - 192.168.137.255 or 192.168.100.0 - 192.168.100.255, etc depending on your network. pi has hostname pi.local...

personally i use findPi on the play store (an android app)
start ssh connection
--------------------


[download putty](https://www.putty.org), a popular ssh client

make sure ssh is selected, let the default port (22)

enter the pi hostname or ip address found

default user is pi

default password is raspberry

if successful, you should be directed to the pi command line interface !

 
