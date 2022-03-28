
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
#import asyncio
from libqtile import hook
import asyncio


from typing import List  # noqa: F401
import subprocess
from libqtile.log_utils import logger
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
#import libqtile
from libqtile.utils import guess_terminal
import copy
from libqtile import qtile

#from qtile_extras import widget as eWidget
import mywidget
'''from xdg import (
    xdg_cache_home,
    xdg_config_dirs,
    xdg_config_home,
    xdg_data_dirs,
    xdg_data_home,
    xdg_runtime_dir,
    xdg_state_home,
)'''

mod = "mod4"
terminal = "terminator"#guess_terminal()

#iqtile.core.set_keymap(layout="de")

logger.warning("before Wayland")
if qtile.core.name == "x11":
    logger.warning("not using Wayland")
elif qtile.core.name == "wayland":
    logger.warning("using Wayland")
    #import wayland
@hook.subscribe.startup_once
def autostart():
        
    logger.warning("autostart called")
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])
    
    if qtile.core.name == "wayland":
        home = os.path.expanduser('~/.config/qtile/autostart_wayland.sh')
        subprocess.run([home])
    
        #sleep(0.5)
        #qtile.cmd_reconfigure_screens()
        #ilazy.reload_config()
        logger.warning("subprocess runned")
        #qtile.cmd_reconfigure_screens(qtile)
   


keys = [
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

    Key([mod, "control"], "r", lazy.restart() if qtile.core.name != "wayland" else lazy.reload_config() , desc="Restart Qtile"),
    Key([mod, "control"], "c", lazy.reload_config(), desc="reload Config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod, "control"], "i", qtile.cmd_reconfigure_screens(), desc="reconfigure screen"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),


    Key([mod], "x", lazy.simulate_keypress([],"a"), desc="testing stuff"),
]

"""
if qtile.core.name == "wayland":
    keys.extend([    
        Key([mod], "b", lazy.spawn("firefox"), desc="spawn firefox"),
    ])
    mouse.extend([
        Click([], "button4", simulate_keypress(["control"], "Tab")),
        Click([], "button5", simulate_keypress(["control","shift"], "Tab")),
    ])
"""
#groups = [Group(i) for i in "123456789"]

groups = [Group(i) for i in "asd"]
groups.extend([Group("f",spawn=["signal-desktop","whatsapp-for-linux","discord"]),
Group("g",spawn="thunderbird")])
groups.extend([Group(i) for i in"12345"])


for i in groups:
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

layouts = [
    layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='sans',
    fontsize=15,
    padding=10,
)
extension_defaults = widget_defaults.copy()


def bottomBar():
    return bar.Bar(
        [
            widget.CurrentLayout(),
            widget.GroupBox(),
            widget.Prompt(),
            widget.WindowName(),
            widget.Chord(
                chords_colors={
                    'launch': ("#ff0000", "#ffffff"),
                },
                name_transform=lambda name: name.upper(),
            ),
            widget.Clock(format='%A %B %d.%m.%Y %H:%M:%S'),
            widget.QuickExit(),        
        ],
        24,
    )


rolloPosToSet = -1

def getRolloPos():
    if rolloPosToSet != -1:
        return str(rolloPosToSet)
    result = subprocess.check_output(["python", "/home/silas/.config/qtile/mywidget/rollo.py","get"],encoding='utf8')
    #logger.warning(result)
    return str(result).replace("\n","")


async def changeRollo(val):
    global rolloPosToSet
    #logger.error("test")
    logger.error("changeRollo rolloPos ")
     
    logger.error(str(rolloPosToSet))
    logger.error("val:")
    logger.error(str(val))
    if rolloPosToSet == -1:
        logger.error("in if")
        toSet = int(getRolloPos())

    else:
        logger.error("in else")
        toSet = rolloPosToSet
   

    logger.error("getRolloPos(): "+str(getRolloPos()) + " as int:" + str(int(getRolloPos())))
    logger.error("toSet before add:"+str(toSet))
    toSet+=val

    logger.error("toSet after add:"+str(toSet))
    
    if toSet<0 or toSet > 100:
        logger.error("toSet ("+str(toSet)+") out of scope returning")
        return
   
    
    logger.error("rolloPosToSet")

    logger.error(str(rolloPosToSet))
    rolloPosToSet = toSet
    await asyncio.sleep(1)
    logger.error(str(rolloPosToSet))

    logger.error(str(rolloPosToSet==toSet))
    if rolloPosToSet == toSet:
        result = subprocess.check_output(["python", "/home/silas/.config/qtile/mywidget/rollo.py","set", str(rolloPosToSet)],encoding='utf8')
    
    rolloPosToSet = -1

def increseRollo():
    logger.error("increseRollo")
    global rolloPosToSet
    logger.error("1")
    logger.error(str(rolloPosToSet))
    logger.error("2")
    asyncio.create_task(changeRollo(5))


def decreseRollo():
    global rolloPosToSet
    logger.error("decreseRollo")
    asyncio.create_task(changeRollo(-5))


#mySystray = widget.Systray()
first = False

spacer = widget.Spacer(length=15)
#widget.Bluetooth(),
cpu= widget.CPU()
sep=widget.Sep()
#mpris2=widget.Mpris2(name="spotifyd",objname="org.mpris.MediaPlayer2.spotifyd",)
#widget.Sep(),
#widget.Mpris2(name="spotifyd",objname="org.mpris.MediaPlayer2.spotify",),
#widget.Sep(),
#widget.Mpris(name='clementine', stop_pause_text='', **widget_defaults),
#widget.Sep(),
cmus=widget.Cmus()
#widget.Sep(),
cpuGraph=widget.CPUGraph()
nvidiaSensor=widget.NvidiaSensors()
memmory=widget.Memory()
checkUpdates=widget.CheckUpdates()
clipboard=widget.Clipboard()
systray=widget.Systray() if qtile.core.name != "wayland" else widget.StatusNotifier()
#mySystray, #if first else widget.TextBox(""), 
#widget.StatusNotifier(),
vol=widget.Volume()
launchBar=widget.LaunchBar([("thunderbird","thunderbird","halt Thunderbird"),("spotify","spotify","startet Spotify")])

rollo = widget.GenPollText(
    update_interval=1,
    func=getRolloPos,
    mouse_callbacks={
        "Button4": increseRollo,
        "Button5": decreseRollo,
    },
)




try:
    
    playerctl= widget.Playerctl()
except Exception as e:
    logger.error("could not use playerctl: ")
    logger.error(e)
        

def topBar():
    global first
    first != first
    return [
        spacer,
        cpu,
        sep,
        #mpris2,
        sep,
        cmus,
        sep,
        cpuGraph,
        nvidiaSensor,
        memmory,
        checkUpdates,
        clipboard,
        #systray,
        vol,
        launchBar,
        playerctl,
        widget.TextBox(qtile.core.name),
        widget.TextBox("rollo"),
        rollo,
    ]

def find_brightnes(idx):
    brightnises = []
    result = subprocess.check_output(["xrandr", "--verbose"],encoding='utf8')
    #logger.error(str(result))   

    for line in result.split("\n"):
        line = line.lower()
        #logger.warning(str(line))


        if "brightnes" in line:
            #logger.warning("found"+str(line))

            line = line.split(":")[1].strip()
            brightnises.append(line)
    #logger.warning(str(brightnises))
    with open("/home/silas/tmp/output.txt","w") as f:
        #logger.warning("wrote: "+str(brightnises))
        f.write(str(result))
    if brightnises == [] or len(brightnises)<= idx:
        return "error"
    
    return str(float(brightnises[idx])*100)
        
#logger.error(str(topBar))



def change_brightness(id, value):
    new_brightness = str(float(find_brightnes(id)) + (value*10))
    logger.error("find: "+str(float(find_brightnes(id))))
    logger.error("id: "+str(id))

    logger.error("value: "+str(value*10))
    logger.error("value*10: "+str(value*10))
    logger.error("ges: "+str(float(find_brightnes(id)) + (value*10)))
    command = "sh /home/silas/.config/qtile/brightniss_control.sh "+str(id)+" "+new_brightness
    logger.error("command: "+str(command))
    qtile.cmd_spawn(command)

def increseBrightness0():
    change_brightness(0,1)

def increseBrightness1():
    change_brightness(1,1)
def increseBrightness2():
    change_brightness(2,1)
def decreseBrighness0():
    change_brightness(0,-1)
def decreseBrighness1():
    change_brightness(1,-1)
def decreseBrighness2():
    change_brightness(2,-1)


def get_top_bar_with_brightness(idx):
    top = topBar()
    if qtile.core.name == "x11":
        top.append(
            widget.GenPollText(
                update_interval=1,
                func=lambda: find_brightnes(idx),
                mouse_callbacks={
                    "Button4": increseBrightness0 if idx==0 else increseBrightness1 if idx==1 else increseBrightness2,
                    "Button5": decreseBrighness0 if idx==0  else decreseBrighness1 if idx==1 else decreseBrighness2,
                },
            )
        )
    return top

top = get_top_bar_with_brightness(2)

#top.append(widget.TextBox("hallo"))

myScreen = Screen(
    wallpaper="/usr/share/backgrounds/archlinux/split.png",
    wallpaper_mode="fill",
    bottom=bottomBar(),
    top=bar.Bar(top,30),
)
#print("hallo")
#print(type(myScreen))
screens = [
        myScreen,
        Screen(
            wallpaper_mode="fill",
            wallpaper="/usr/share/backgrounds/archlinux/wave.png",
            bottom=bottomBar(),
            top=bar.Bar(
                get_top_bar_with_brightness(0),
                30,
            )
        ),
        Screen(
            wallpaper="/usr/share/backgrounds/archlinux/archwave_High.png",
            wallpaper_mode="fill",
            bottom=bottomBar(),
            top=bar.Bar(
                get_top_bar_with_brightness(1),
                30,
            )
        )
    ]
#screens=[myScreen,widget.Mirror(myScreen)]


# Drag floating layouts.
#def foucsCurrent(window):
#    if not self.qtile.config.follow_mouse_focus and self.group.currentWindow != lazy.window:
#        self.group.focus(self, False)
"""
@hook.subscribe.startup_once
async def _():
    logger.warning("start reconfigure")
    await asyncio.sleep(0.5)
    qtile.cmd_reconfigure_screens()
    logger.warning("end reconfigure")
"""


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
    #Click(["mod1"],"Button2",foucsCurrent(lazy.window)),
    #Click(["mod1"], "Button2", focus_hovered()),
    

    Click([mod, "control"], "Button1", lazy.window.toggle_floating())

]


if qtile.core.name == "wayland":
    keys.extend([    
        Key([mod], "b", lazy.spawn("firefox"), desc="spawn firefox"),
        Key([mod], "v", lazy.spawn("clipman pick -t wofi"), desc="clipboard Menu"),
    ])
    mouse.extend([
        Click([], "Button8", lazy.spawn("ydotool key 42:1 29:1 15:1 15:0 29:0 42:0")),
        #Click([], "Button9", lazy.spawn("ydotool key 29:1 15:1 15:0 29:0")),
    ])
else:
    mouse.extend([
        Click([], "Button9", lazy.spawn("terminator")),
    ])

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = False 
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
