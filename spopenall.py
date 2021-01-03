#!/usr/bin/python3

#This script finds all the (hidden) scratch pad window and opens them

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

if __name__ == "__main__":
    i3 = i3ipc.Connection()
    tree = i3.get_tree()
    scWindows = tree.scratchpad().leaves()
    # find leaves that have a scratch pas status
    # print(leaves[0].ipc_data)
    for win in scWindows:
        win.command("focus")
