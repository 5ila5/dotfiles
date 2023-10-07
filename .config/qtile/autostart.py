from libqtile import qtile
import os
from libqtile import hook
import subprocess
import get_core
from pc_type import laptop
from wayland_env_vars import WAYLAND_ENV_VARS


currentDir =  os.path.dirname(os.path.realpath(__file__))+ "/"



def autostart():
    
    home = os.path.expanduser(currentDir+'autostart.sh')
    subprocess.run([home])
    
    if get_core.get_core_name()== "wayland":
        home = os.path.expanduser(currentDir+'autostart_wayland.sh')
        os.environ.update(WAYLAND_ENV_VARS)
    else:
        home = os.path.expanduser(currentDir+'autostart_X11.sh')
    subprocess.run([home])
    
    if laptop:
        home = os.path.expanduser(currentDir+'autostart_laptop.sh')
    subprocess.run([home])
    
