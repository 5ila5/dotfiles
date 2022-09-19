# Copyright (c) 2014 Sean Vig
# Copyright (c) 2014 roger
# Copyright (c) 2014 Tycho Andersen
# Copyright (c) 2014 Adi Sieker
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

from datetime import datetime, timedelta
from libqtile import qtile
from libqtile.lazy import lazy

#from libqtile.widget import base

# import required module
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio
import os


#class Countdown(base.InLoopPollText):
selected=1
format="{H}h {M}m {S}s"
mod_format=["{H}h {M}m >{S}s", "{H}h >{M}m {S}s", ">{H}h {M}m {S}s"]
mod_time=[timedelta(seconds=1),timedelta(minutes=1),timedelta(hours=1)]



timer_delta=timedelta()
date = datetime.now()
started = False
playback = False
playback_pid=-1

def select_next():
    global selected
    selected= selected+1
    if selected >= 3:
        selected=0
    update()


def poll():
    global date
    global started
    global timer_delta
    global playback
    global selected
    
    if playback:
        return "**ALARM**"
     
    now = datetime.now()
    
    if not started:
        date = datetime.now() + timer_delta
    else:
        if date < now:  
            started=False
            finished()
            return "**ALARM**!!"
        

    days = hours = minutes = seconds = 0
    delta = date - now
    
    if not date < now:  
        days = delta.days
        hours, rem = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(rem, 60)

    data = {
        "D": "%02d" % days,
        "H": "%02d" % hours,
        "M": "%02d" % minutes,
        "S": "%02d" % seconds,
    }
    if started:
        return format.format(**data)

    return mod_format[selected].format(**data)


def timer_scroll_up():
    global timer_delta
    global selected
    global mod_time
    
    timer_delta = timer_delta + mod_time[selected]  
    update()
    
    
def timer_scroll_down():
    global timer_delta
    global selected
    global mod_time
    
    if timer_delta>timedelta():
    
        timer_delta = timer_delta - mod_time[selected] 
        if timer_delta<timedelta():
            timer_delta = timedelta() 
        update()

        
    
def cancel():
    global date
    global timer_delta
    global started    

    
    started = False
    date=datetime.now()
    timer_delta=timedelta()
    

def start_pause():
    global started
    global timer_delta
    global date
    global playback
    global playback_pid
    
    
    if playback: #Stop Alarm
        #playback.stop()
        playback=False
        if playback_pid != -1:
            qtile.cmd_spawn("kill "+str(playback_pid))
            qtile.cmd_spawn("alacritty -t kill "+str(playback_pid))
            playback_pid = -1
            update()
            
    
    elif started: #Pause Timer
        started=False
        timer_delta = date - datetime.now()
    else: #start Timer
        if timer_delta > timedelta():
            date = datetime.now()+timer_delta
            started=True
            update()
            
            
def update():
    w = qtile.widgets_map["timerwidget"]
    w.update(w.poll())
    
    
def finished():
    global timer_delta
    global playback
    global playback_pid
        
    timer_delta = timedelta()
    folder = os.path.dirname(os.path.abspath(__file__))
    
    playback=True
    playback_pid=qtile.cmd_spawn("mpg123 "+ folder+"/alarm.mp3")

    #qtile.cmd_spawn("alacritty -t "+str(pid))
    
    
    #playback = _play_with_simpleaudio(song)
        
