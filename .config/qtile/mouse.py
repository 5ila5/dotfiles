from libqtile.config import Click, Drag
from libqtile.lazy import lazy
import os
currentDir = os.path.dirname(os.path.realpath(__file__))+"/"
with open(currentDir+"modKey.conf","r") as f:
    mod = f.read().replace("\n","")


def init_mouse() ->list:
    mouse = [
        Drag([mod], "Button1", lazy.window.set_position_floating(),
            start=lazy.window.get_position()),
        Drag([mod], "Button3", lazy.window.set_size_floating(),
            start=lazy.window.get_size()),
        Click([mod], "Button2", lazy.window.bring_to_front()),
        #Click([],"Button2",foucsCurrent(lazy.window)),
        #Click([], "Button2", focus_hovered()),
        
        #Click([], "Button2", lazy.window.set_position_floating()),

        Click([mod, "control"], "Button1", lazy.window.toggle_floating()),

    ]
    return mouse

def add_wayland_specific_mouse(mouse:list) -> list:
    mouse.extend([
        Click([], "Button8", lazy.spawn("ydotool key 42:1 29:1 15:1 15:0 29:0 42:0")),
        Click([], "Button9", lazy.spawn("ydotool key 29:1 15:1 15:0 29:0")),
    ])
    return mouse
def add_X11_specific_mouse(mouse:list) -> list:
    mouse.extend([])
    return mouse
