from libqtile.config import Key, Group
from libqtile.lazy import lazy
from get_core import get_core_name
import os
import typing
currentDir =  os.path.dirname(os.path.realpath(__file__))+ "/"
with open(currentDir+"modKey.conf","r") as f:
    mod = f.read().replace("\n","")

terminal = "alacritty"

def init_keys() -> typing.List[Key]:

    return [
        # Switch between windows
        Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
        Key([mod], "space", lazy.layout.next(),
            desc="Move window focus to other window"),

        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
            desc="Move window to the left"),
        Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
            desc="Move window to the right"),
        Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
            desc="Move window down"),
        Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key([mod, "control"], "h", lazy.layout.grow_left(),
            desc="Grow window to the left"),
        Key([mod, "control"], "l", lazy.layout.grow_right(),
            desc="Grow window to the right"),
        Key([mod, "control"], "j", lazy.layout.grow_down(),
            desc="Grow window down"),
        Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack"),
        Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

        # Toggle between different layouts as defined below
        Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
        Key(["mod1"], "F4", lazy.window.kill(), desc="Kill focused window"),

        Key([mod, "control"], "r", lazy.restart() if get_core_name() != "wayland" else lazy.reload_config() , desc="Restart Qtile"),
        Key([mod, "control"], "c", lazy.reload_config(), desc="reload Config"),
        Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
        #Key([mod, "control"], "i", qtile.cmd_reconfigure_screens(), desc="reconfigure screen"),
        Key([mod], "r", lazy.spawn("sh /home/silas/.config/qtile/spawn.sh"),
            desc="Spawn a command using a prompt widget"),
        Key([mod], "e", lazy.spawn("nemo"),
            desc="Spawn a command using a prompt widget"),
        
        Key([mod, "shift"], "r", lazy.spawncmd(),
            desc="Spawn a command using a prompt widget"),
        Key([mod], "x", lazy.simulate_keypress([],"a"), desc="testing stuff"),
    ]


def assigne_group_keys(keys : typing.List[Key],  groups: typing.List[Group]) -> typing.List[Key]:
    for i in groups:
        if i.name == "key":
            keys.append(Key([mod], "k", lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name))),
            continue
        
        keys.extend([
            # mod1 + letter of group = switch to group
            Key([mod], i.name, lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name)),

            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(i.name)),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ])
    return keys



def wayland_specific_keys(keys : typing.List[Key]) -> typing.List[Key]:
    keys.extend([    
        Key([mod], "b", lazy.spawn("firefox"), desc="spawn firefox"),
        Key([mod], "v", lazy.spawn("clipman pick -t wofi"), desc="clipboard Menu"),
    ])
    return keys

def X11_specific_keys(keys : typing.List[Key]) -> typing.List[Key]:
    keys.extend([])
    return keys
