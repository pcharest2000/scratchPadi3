#!/usr/bin/env python3

#This scrip uses dmenu or rofi to fetch windows in the i3 sratch pad and presents
#a menu to select one and brinf it to the front

# Author, current maintainer: Philippe Charest <philippe.charest@gmail.com>

# Copyright (C) 2020

# This program is free software which I release under the GNU General Public
# License. You may redistribute and/or modify this program under the terms
# of that license as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# To get a copy of the GNU General Puplic License,  write to the
# Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import i3ipc
import os
#Select which executable you want to use
MENUEXEC="rofi -dmenu"
#MENUEXEC="dmenu"
if __name__ == "__main__":
    i3 = i3ipc.Connection()
    tree = i3.get_tree()
    scWindows = tree.scratchpad().leaves()
    winMenuString = '"'
    winDict = {}
    count = 0  # Used to enumarate windows with same title
    for win in scWindows:
        winDict[str(count) + ": " + win.name] = win
        winMenuString += str(count) + ": " + win.name + "\n"
        count += 1
    winMenuString = winMenuString[:-1]  # Remvoe the extra \n
    winMenuString += '"'
    commandString = (
        "echo " + winMenuString + '| ' + MENUEXEC+  ' -p "Select Scratchpad window to open"'
    )
    menuout = os.popen(commandString, "r").read()
    menuout = menuout[:-1]  # For some reason read returns an extra \n
    if menuout == "":
        print("No window selected")
    else:
        winDict[menuout].command("focus")  # command to close all windows

