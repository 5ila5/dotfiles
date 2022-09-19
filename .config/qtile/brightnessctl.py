import subprocess
import time
from libqtile import qtile

class Brightnessctl:
    last_brightness = -1
    display_id = 1
    text = ''
    changed = False
    new_val = 50
    cap = 100

    def __init__(self,display_id,text="Helligkeit: "):
        self.display_id = display_id
        self.text = text


    def get_brighness_text(self):
        if self.last_brightness == -1:
            time.sleep(self.display_id-1)
            self.update_brightness()
        if self.changed:
            return self.text + str(self.new_val) + "?"

        return self.text + str(self.last_brightness)

    def update_brightness(self):
        self.last_brightness, cap = get_brightness(self.display_id)

        if cap != -1:
            self.cap = cap

    def click(self):

        if self.changed:
            self.last_brightness = self.new_val
            change_brightness(self.display_id, self.new_val, self.cap)
            self.changed = False
            return
        
        self.changed = False
        self.update_brightness()
        self.update()
        


    def scroll(self, direction):
        if not self.changed:
            #self.update_brightness()
            self.new_val = self.last_brightness
            self.changed = True
        
        self.new_val += 5 * direction - self.new_val % 5

        if self.new_val < 10:
            self.new_val = 10
        elif self.new_val > 100:
            self.new_val = 100
        if self.new_val == self.last_brightness:
            self.changed= False
        
        self.update()
        



    def scroll_up(self):
        self.scroll(1)

    def scroll_down(self):
        self.scroll(-1)

    def cancel(self):
        self.changed = False
        self.update_brightness()
        self.update()

    def __int__(self):
        return int(self.display_id)
    
    def __str__(self):
        return "Brightnessctl for Display "+ str(self.display_id)
    def update(self):
        w = qtile.widgets_map["brightnessctl"+str(self.display_id)]
        w.update(w.poll())


def get_brightness(display_id) -> int:
    output = subprocess.check_output(["ddcutil", "getvcp", "10", "--brief", "--display",str(display_id)]).decode().replace("\n","")
    if "failed" in output or "not found" in output:
        return -1,-1
    
    out_arr = output.split(" ")


    if len(out_arr) != 5 or not out_arr[3].isdigit() or not out_arr[4].isdigit():
        return -1,-1

    return int(int(out_arr[3])/int(out_arr[4])*100), int(out_arr[4])


def change_brightness(display_id, new_val, cap ) -> bool:
    print("change_br")
    command = ["ddcutil", "setvcp", "10", "--brief", "--display", str(display_id), str(int((new_val/100)*cap))]
    print(command)
    subprocess.check_output(command)
    