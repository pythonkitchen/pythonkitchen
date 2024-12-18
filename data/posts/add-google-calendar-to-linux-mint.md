title: Add Google Calendar Desklet To Linux Mint 22
slug: add-google-calendar-desklet-linux-mint
pub: 2024-12-18 16:42:02
authors: arj
tags: linux


[Google Calendar Desklet](https://cinnamon-spices.linuxmint.com/desklets/view/35) is a Python-packaged desklet app for Linux.

[gcalendar](https://github.com/slgobinath/gcalendar) is a Python cli for getting Google calendar events.

The desklet uses it to show events.

## Installation

Installing gcalendar is best done through apt


```
sudo add-apt-repository ppa:slgobinath/gcalendar
sudo apt update
sudo apt install gcalendar
```

Then write `gcalendar` on the terminal and configure.

Then you right click on desktop -> Add desklet -> Download -> Google calendar -> Click on the download icon.

The go to manage -> Google calendar -> Click on the + sign

Then the configure icon will be ready, click and add your calendars.

You can click on the `Click on the list below with the names of all my calendars`