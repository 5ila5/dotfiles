import rollo
from libqtile import qtile
import brightness_control
from libqtile.config import Screen
from libqtile import bar, layout, widget
import get_core
from brightness_control import *
import typing

core_name = get_core.get_core_name()


colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]


playerctl= widget.Playerctl()
#widget.Bluetooth(),
cpu= widget.CPU()
#sep=widget.Sep()
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
#systray=widget.Systray() if core_name != "wayland" else widget.StatusNotifier()
#mySystray, #if first else widget.TextBox(""), 
#widget.StatusNotifier(),
vol=widget.Volume(device="pulse")
corenamewidget = widget.TextBox(core_name),
rollotextwidget = widget.TextBox("rollo"),

mySep = widget.TextBox(
        text = '◀',
        font = "Ubuntu Mono",
        background = colors[0],
        foreground = colors[3],
        padding = 0,
        fontsize = 37
        )

rollo = widget.GenPollText(
    update_interval=1,
    func=rollo.getRolloPos,
    mouse_callbacks={
        "Button4": rollo.increseRollo,
        "Button5": rollo.decreseRollo,
    },
)

def init_layouts()->list:
    layouts = [
        layout.Columns(border_focus='#009926', border_focus_stack=['#009926', '#009926'],  border_width=2),
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
    return layouts

def init_widget_defaults() -> dict:
    return dict(
        font='sans',
        fontsize=15,
        padding=10,
    )


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
systray = widget.Systray()
def init_widget_list(idx) -> list:
    to_return = [            
        widget.Spacer(10),
        #mySep,
        cpu,
        #sep,
        #mpris2,
        #sep,
        cmus,
        #sep,
        cpuGraph,
        nvidiaSensor,
        memmory,
        checkUpdates,
        clipboard,
    ]
    if core_name == "wayland":
        to_return.extend([])
    else:
        pass
        '''to_return.extend([
            #systray,
            widget.TextBox("helligkeit"),
            widget.TextBox("idx:"+str(idx)),
            widget.GenPollText(
                update_interval=5,
                func=lambda: find_brightnes(idx),
                mouse_callbacks={
                    "Button4": increseBrightness0 if idx==0 else increseBrightness1 if idx==1 else increseBrightness2,
                    "Button5": decreseBrighness0 if idx==0  else decreseBrighness1 if idx==1 else decreseBrighness2,
                },
            )
        ])'''

    if idx==2:
        to_return.extend([systray]) 
    to_return.extend([
        widget.StatusNotifier(),
        #systray,
        vol,
        playerctl,
        widget.LaunchBar(progs=[("thunderbird","thunderbird","halt Thunderbird"),("spotify","spotify","startet Spotify")]),
        #core_name_widget,
        widget.TextBox(core_name),
        #rollo_text_widget,
        widget.TextBox(str(idx)),
        #rollo,
    ])
    return to_return
    


def topBar(idx)-> bar.Bar:
    return bar.Bar(
        init_widget_list(idx),
        30,
    )


def init_screens() -> typing.List[Screen]:
    #screens = 
    return [
        Screen(
            wallpaper="/usr/share/backgrounds/archlinux/split.png",
            wallpaper_mode="fill",
            bottom=bottomBar(),
            top=topBar(2),
        ),
        Screen(
            wallpaper="/usr/share/backgrounds/archlinux/archwave_High.png",
            wallpaper_mode="fill",
            bottom=bottomBar(),
            top=topBar(0)
        ),
        Screen(
            wallpaper_mode="fill",
            wallpaper="/usr/share/backgrounds/archlinux/wave.png",
            bottom=bottomBar(),
            top=topBar(1),
        ),
        
    ]
    #return screens

