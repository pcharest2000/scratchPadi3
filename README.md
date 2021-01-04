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
-With your favorite editor Modify the script variable MENUEXEC to choose between rofi or dmenu  
-Make the script executable: chmod + x spselect.py  
-Copy the script somewhere in your path:  
  cp spselect.py ~/.local/bin  

Bind the script in your i3 config file with the proper argument:  
bindsym $mod+Ctrl+s  exec "${HOME}/.local/bin/spselect --select"  

# Usage
<pre>
usage: spselect.py [-h] [--select] [--showall] [--hideall]  

optional arguments:  
  -h, --help  show this help message and exit  
  --select    Shows a dmenu/rofi menu to select a window in the  
              scratchpad  
  --showall   Show all windows from the scratchpad  
  --hideall   Put back all scratcpad window to the scratchpad  
</pre>

