import rolloctl
from libqtile import qtile
from brightnessctl import Brightnessctl 
from libqtile.config import Screen, Match
from libqtile import bar, layout
from libqtile.log_utils import logger

import get_core
core_name = get_core.get_core_name()
qtile_extra = False
try:
    if core_name == "wayland":
        from qtile_extras import widget
        # from qtile_extras.widget import PulseVolume
        # from generic_progress_bar_widget import GenericProgressBar
        from qtile_extras.widget.mixins import ExtendedPopupMixin, ProgressBarMixin, TooltipMixin
        qtile_extra = True
    else:
        from libqtile import widget
except ImportError as e:
    from libqtile import widget
    logger.warning("could not import all or some qtiles_extras functunallity falling back to default widgets", e)

from libqtile.lazy import lazy
import typing
import datetime
import timer
from pc_type import laptop
from mywidgets.playerctl.playerctl import Playerctl



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


playerctl= Playerctl()
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
vol=widget.Volume()#device="pulse")
corenamewidget = widget.TextBox(core_name),
rollotextwidget = widget.TextBox("rollo"),

dateCountTo = datetime.datetime.now()#datetime(2022, 10, 17, 21, 29, 13, 621094)
dateCountTo = dateCountTo + datetime.timedelta(minutes=1)
#pVol = widget.PulseVolume()


if qtile_extra:
    class OpenWeatherTooltip(widget.OpenWeather, TooltipMixin):
        defaults = [(
                "tooltip_format",
                "",
                "Display tooltip format format",
            )]
        
        def __init__(self, **config):
            widget.OpenWeather.__init__(self, **config)
            TooltipMixin.__init__(self, **config)
            self.add_defaults(TooltipMixin.defaults)
            self.add_defaults(OpenWeatherTooltip.defaults)
            self.tooltip_text = ""

        def parse(self, response):
            original_format = self.format
            self.format = self.tooltip_format
            self.tooltip_text = super().parse(response)
            self.format = original_format
            return super().parse(response)
       

    class BacklightBar(widget.Backlight, ProgressBarMixin):
        def __init__(self, **config):
            widget.Backlight.__init__(self, **config)
            ProgressBarMixin.__init__(self, **config)
            self.add_defaults(widget.Backlight.defaults)
            self.add_defaults(ProgressBarMixin.defaults)

        def _get_info(self):
           val = super()._get_info()
           self.bar_draw(bar_value=val)
           return val 
            
try:
    from api_keys import openweather_api_key, weather_location
    weather = widget.OpenWeather(
        app_key=openweather_api_key,
        location=weather_location,
        language="de",
        format='{location_city}: {icon} {main_temp} °{units_temperature} ({main_temp_min}°{units_temperature} — {main_temp_max}°{units_temperature})  {weather_details}'
    )
    if qtile_extra:
        weather = OpenWeatherTooltip(
            app_key=openweather_api_key,
            location=weather_location,
            language="de",
            format='{icon} {main_temp} °{units_temperature}',
            tooltip_format='{location_city}: {icon} {main_temp} °{units_temperature} ({main_temp_min}°{units_temperature} — {main_temp_max}°{units_temperature})  {weather_details}'
        )


except ImportError:
    weather = widget.TextBox("no API KEY")#widget.OpenWeather(location="Seeheim, DE")
#weather = widget.OpenWeather(location="Seeheim, DE")
    
timerwidget = widget.GenPollText(
    update_interval=1.0,
    func=timer.poll,
    name="timerwidget",
    mouse_callbacks={
        "Button1": timer.start_pause,
        "Button2": timer.select_next,
        "Button3": timer.cancel,
        "Button4": timer.timer_scroll_up,
        "Button5": timer.timer_scroll_down,
    }
)


"""timerwidget = widget.Countdown(date=dateCountTo, mouse_callbacks={
        "Button4": timer_scroll_up,
        "Button1": timer_scroll_up,
        "Button2": timer_scroll_up,
        "Button3": timer_scroll_up,
        
        "Button5": timer_scroll_down,
    })"""



mySep = widget.TextBox(
        text = '◀',
        font = "Ubuntu Mono",
        background = colors[0],
        foreground = colors[3],
        padding = 0,
        fontsize = 37
        )

rollo = widget.GenPollText(
    name="rolloctl",
    update_interval=.3,
    func=rolloctl.get_rollo_text,
    mouse_callbacks={
        "Button1": rolloctl.click,
        "Button2": rolloctl.blendet,
        "Button3": rolloctl.cancel,
        "Button4": rolloctl.scroll_up,
        "Button5": rolloctl.scroll_down,
    }
)


def init_floating_layout():
    return layout.Floating(
        float_rules=[
            *layout.Floating.default_float_rules,
            Match(wm_type='menu'),
            Match(wm_class='confirm'),
            Match(wm_class='dialog'),
            Match(wm_class='download'),
            Match(wm_class='error'),
            Match(wm_class='file_progress'),
            Match(wm_class='notification'),
            Match(wm_class='splash'),
            Match(wm_class='toolbar'),
            Match(wm_class='confirmreset'),
            Match(wm_class='makebranch'),
            Match(wm_class='maketag'),
            Match(title='branchdialog'),
            Match(title='pinentry'),
            Match(wm_class='ssh-askpass'),
            Match(title='Xephyr on :1.0 (ctrl+shift grabs mouse and keyboard)'),
            Match(title='Bitwarden'),
            Match(wm_class='nextcloud'),
            Match(wm_class='system-config-printer'),
    ]) 


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
        layout.VerticalTile(border_normal='#000000',),# border_focus='#009926', border_focus_stack=['#009926', '#009926']),

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
            # weather,
            widget.CurrentLayout(),
            widget.GroupBox(disable_drag=True),
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
brighnestlc = [] # [Brightnessctl(id) for id in range(1,4)]

if not qtile_extra:
    brighnestlc = [Brightnessctl(id) for id in range(1,4)]


def init_widget_list(idx) -> list:    
    to_return = [
        # pVol,
        widget.Spacer(10),
        # GenericProgressBar(
        #     update_interval=30,
        #     name="brightnessctlTEST123",
        #     bar_text_func=brighnestlc[idx].get_brighness_text,
        #     error_func=brighnestlc[idx].get_changed,
        #     value_func=brighnestlc[idx].get_brightness_text_val,
        #     mouse_callbacks={
        #         "Button1": brighnestlc[idx].click,
        #         "Button2": brighnestlc[idx].cancel,
        #         "Button3": brighnestlc[idx].cancel,
        #         "Button4": brighnestlc[idx].scroll_up,
        #         "Button5": brighnestlc[idx].scroll_down,
        #     },
        #     bar_text_max_string = "Helligkeit: 100% ?",
        # ),       
        # widget.Mpris2(),
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

        #brightness_widget,
    ]
    
    if qtile_extra:
        pass
        # to_return.append(GenericProgressBar(
        # # widget.GenPollText(
        #     update_interval=30,
        #     name="brightnessctl"+str(brighnestlc[idx].display_id),
        #     bar_text_func=brighnestlc[idx].get_brighness_text,
        #     error_func=brighnestlc[idx].get_changed,
        #     value_func=brighnestlc[idx].get_brightness_text_val,
        #     mouse_callbacks={
        #         "Button1": brighnestlc[idx].click,
        #         "Button2": brighnestlc[idx].cancel,
        #         "Button3": brighnestlc[idx].cancel,
        #         "Button4": brighnestlc[idx].scroll_up,
        #         "Button5": brighnestlc[idx].scroll_down,
        #     },
        #     bar_text_max_string = "Helligkeit: 100% ?",
        # ))
    else:
        to_return.append(widget.GenPollText(
            update_interval=30,
            name="brightnessctlc"+str(brighnestlc[idx].display_id),
            func=brighnestlc[idx].get_brighness_text,
            mouse_callbacks={
                "Button1": brighnestlc[idx].click,
                "Button2": brighnestlc[idx].cancel,
                "Button3": brighnestlc[idx].cancel,
                "Button4": brighnestlc[idx].scroll_up,
                "Button5": brighnestlc[idx].scroll_down,
            },
            bar_text_max_string = "Helligkeit: 100% ?",
        ))
    
    if core_name == "wayland":
        to_return.extend([widget.StatusNotifier()])
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
        #systray,
        weather,
        vol,
        timerwidget,
        playerctl,
        #widget.LaunchBar(progs=[("thunderbird","thunderbird","halt Thunderbird"),("spotify","spotify","startet Spotify")]),
            widget.LaunchBar(progs=[("/home/silas/Nextcloud/uni/stundenplan.png", "mupdf /home/silas/Nextcloud/uni/stundenplan.png","stundenplan")]),
        #core_name_widget,
        #widget.TextBox(core_name),
        #rollo_text_widget,
        #widget.TextBox(str(idx)),
        rollo,
        weather,
    ])
    return to_return

def topBarLaptop()-> bar.Bar:
    backlight_sens = "2" if core_name != "wayland" else "0.7"
    return bar.Bar(
        [  
        widget.Spacer(10),
        cpu,
        cpuGraph,
        memmory,
        widget.Backlight(
            backlight_name="intel_backlight",
            mouse_callbacks=
            {
                "Button4": lazy.spawn("brillo -q -u 150000 -A " + backlight_sens),
                "Button5": lazy.spawn("brillo -q -u 150000 -U " + backlight_sens),
            }
            ),
        widget.Battery(),
        widget.BatteryIcon(),
        systray if core_name != "wayland" else widget.StatusNotifier(),
        timerwidget,
        playerctl,
        widget.LaunchBar(progs=[("/home/silas/Nextcloud/uni/stundenplan.png","mupdf /home/silas/Nextcloud/uni/stundenplan.png","stundenplan")]),
        vol,
        weather,
        ],
        30
    )
    


def topBar(idx)-> bar.Bar:
    return bar.Bar(
        init_widget_list(idx),
        30,
    )


def init_screens() -> typing.List[Screen]:
    if not laptop:
        screens = [
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
        if core_name == "wayland":
            screens[1], screens[2] = screens[2], screens[1]
        return screens
    else:
        return [
            Screen(
                wallpaper="/usr/share/backgrounds/archlinux/split.png",
                wallpaper_mode="fill",
                bottom=bottomBar(),
                top=topBarLaptop(),
            ),
        ]
    
    #return screens

