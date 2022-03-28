from libqtile import qtile
import os
from libqtile import hook
import subprocess
import get_core

currentDir =  os.path.dirname(os.path.realpath(__file__))+ "/"



def autostart():
    
    home = os.path.expanduser(currentDir+'autostart.sh')
    subprocess.run([home])
    
    if get_core.get_core_name()== "wayland":
        home = os.path.expanduser(currentDir+'autostart_wayland.sh')
    else:
        home = os.path.expanduser(currentDir+'autostart_X11.sh')
    subprocess.run([home])
    
       
