import subprocess
import os
import json
from libqtile.log_utils import logger
from libqtile import qtile


rollo_py_path = "~/.config/HomeassistantAPI_ctl/rollo.py"
rollo_py_path = os.path.expanduser(rollo_py_path)

rollo_to_change = 0
clicked = False
changed = False
changed_to = 0

def get_rollo_text(): 
    if not clicked:
        return ["Fenster","Tür","Beide"][rollo_to_change]
    if not changed:
        command_out = subprocess.check_output(["python3", rollo_py_path,"get",["fenster","tuer",""][rollo_to_change]]).decode().replace("\n","")
        print('subprocess.check_output(["python3",'+ rollo_py_path+', "get",'+["fenster","tuer",""][rollo_to_change]+'])')
        return str(["Fenster","Tür","Beide"][rollo_to_change]+": " + str(command_out)).replace("\n", "")
    return ["Fenster","Tür","Beide"][rollo_to_change]+": "+ str(changed_to) +"?"

def change_rollo_state(direction):
    global rollo_to_change
    print(f"change_rollo_state({direction})")

    rollo_to_change += direction
    if rollo_to_change >2:
        rollo_to_change = 0
    if rollo_to_change <0:
        rollo_to_change = 2

def change_rollo_val(direction):
    global changed_to, changed, rollo_py_path, rollo_to_change
    if not changed:
        changed_to = subprocess.check_output(["python3", rollo_py_path,"get",["fenster","tuer",""][rollo_to_change]]).decode().replace("\n","")
        if "[" in changed_to:
            changed_to = int(json.loads(changed_to)[0])
        else :
            changed_to = int(changed_to)


    if changed_to + direction*5 in range(0,101):
        changed = True
        changed_to += direction*5
        changed_to -= changed_to % 5


def scroll_up():
    print("scroll_up")
    direction = 1
    if clicked:
        change_rollo_val(direction)
        update()
        return
    change_rollo_state(direction)
    update()

def scroll_down():
    direction = -1
    if clicked:
        change_rollo_val(direction)
        update()
        return
    change_rollo_state(direction)
    update()

def click():
    global clicked, changed, changed_to, rollo_to_change
    if not clicked:
        clicked = True
        update()
        return
    
    if changed:
        print("call")
        print("subprocess.call("+str(["python3", rollo_py_path,["--fenster","--tuer","--beide"][rollo_to_change],changed_to])+")")
        
        subprocess.check_output(["python3", rollo_py_path,["--fenster","--tuer","--beide"][rollo_to_change],str(changed_to)])
    clicked = False
    changed = False
    update()
    
def cancel():
    global clicked, changed
    clicked = False
    changed = False
    update()

def debug():
    print(get_rollo_text())
    scroll_up()
    #print(get_rollo_text())
    scroll_up()
    print(get_rollo_text())

    click()
    print(get_rollo_text())

    scroll_down()
    print(get_rollo_text())
    scroll_down()
    print(get_rollo_text())

    click()

def blendet():
    subprocess.check_output(["python3", rollo_py_path])

def update():
    w = qtile.widgets_map["rolloctl"]
    w.update(w.poll())
    


if __name__ == "__main__":
    debug()