# scratchPadi3
Python script to managei i3 scratchpad winddows

# Requirements
-i3! (Dohh)  
-Python3  
-i3ipc:  pip (or pip3) install i3ipc  

# Install
-pip  install i3ipc  
-git clone https://github.com/pcharest2000/scratchPadi3.git  
-cd scratchPadi3  
-chmod + x spselect.py  
Copy the scrip somewhere in your path.  

Bind them in your i3 config file:  
bindsym $mod+Ctrl+s  exec "${HOME}/.local/bin/spselect --select"  

# Usage
usage: spselect.py [-h] [--select] [--showall] [--hideall]  

optional arguments:  
  -h, --help  show this help message and exit  
  --select    Shows a dmenu/rofi menu to select a window in the  
              scratchpad  
  --showall   Show all windows from the scratchpad  
  --hideall   Put back all scratcpad window to the scratchpad  


