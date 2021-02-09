# Introduction
This repository contains code for displaying a slideshow menu on a TV in a restaurant or bar. You can add special menu items to the menu that will only appear on certain days of the week.

This code is designed to be used on a Raspberry Pi that is connected to a TV screen via HDMI.
    
# Getting Started
* **Clone the menu repository from GitHub to your Raspberry Pi**
    * run:
        * git clone https://github.com/lukerbs/menu.git
* **Get your menu images**
    * Copy your menu images into the **/imgs/** directory
    * In **menu_display.py**, add your desired menu photos file names to **weekday_menu**, **weekend_menu**, and **friday_menu** lists respectively
* **Dependencies**
    * There are a few Python dependencies required to run the code. If the dependencies are not already installed on your Raspberry Pi you are using, install them with the following command:
    * Run:
        * pip3 pygame screeninfo
# Starting the Menu
* cd into the menu repository and run **python3 menu_display.py**
* The menu will display in full screen on the TV until you turn off the Raspberry Pi
