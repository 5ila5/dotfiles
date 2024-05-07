
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
import asyncio


from typing import List  # noqa: F401
import subprocess
from libqtile.log_utils import logger
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
#import libqtile
import copy
from libqtile import qtile

import sys
#import importlib
# Config imports
'''def reload(module):
    if module in sys.modules:
        importlib.reload(sys.modules[module])

reload("autostart")
reload("brightnesscontrol")
reload("get_core")
reload("groups")
reload("keys")
reload("mouse")
reload("rollo")
reload("screens")
'''


terminal = "terminator"

# My imports
import autostart 
from keys import init_keys, assigne_group_keys, wayland_specific_keys, X11_specific_keys
from screens import  init_layouts, init_widget_defaults, init_screens
from get_core import get_core_name
from groups import init_groups
from mouse import init_mouse, add_wayland_specific_mouse, add_X11_specific_mouse


from libqtile.backend.wayland import InputConfig
wl_input_rules = {
    "type:touchpad": InputConfig(tap_button_map="lrm", middle_emulation=True, tap=True),
}

@hook.subscribe.startup_once
def startup():
    autostart.autostart()

keys = init_keys()
groups = init_groups()
keys = assigne_group_keys(keys, groups)
layouts = init_layouts()
widget_defaults = init_widget_defaults()
extension_defaults = widget_defaults.copy()
mouse = init_mouse()
screens = init_screens()
#logger.error(str(screens))
if get_core_name() == "wayland":
    qtile.core.set_keymap(layout="de", options="caps:escape,shift:both_capslock_cancel" )
    keys = wayland_specific_keys(keys)
    mouse = add_wayland_specific_mouse(mouse)

else:
    mouse = add_X11_specific_mouse(mouse)
    keys = X11_specific_keys(keys)


#logger.error(str(keys))
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = True 
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
