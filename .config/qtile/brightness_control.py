from libqtile.log_utils import logger
import subprocess
from libqtile.lazy import lazy


brightnises = ["100","100","100"]
bussy = False

def find_brightnes_old(idx):
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
    #with open("/home/silas/tmp/output.txt","w") as f:
    #logger.warning("wrote: "+str(brightnises))
    #f.write(str(result))
    if brightnises == [] or len(brightnises)<= idx:
        return "error"
    
    return str(float(brightnises[idx])*100)
        
#logger.error(str(topBar))

def getBrghnisses(arr):
    global brightnises
    for i in arr:
        result = subprocess.check_output(["ddcutil", "getvcp", "10", "-d", str(i), "--brief"],encoding='utf8')
        #logger.error(str(result))   

        result = result.split(" ")

        max_b = int(result[4])
        curr_b = int(result[3])
        brightnises[i-1] =  str(float(curr_b/max_b)*100)

def find_brightnes(idx):
    global bussy, brightnises
    logger.warning(str(brightnises))
    if bussy:
        
        logger.warning(str(idx)+":")

        logger.warning(brightnises[idx])
        return brightnises[idx]
    else:
        bussy = True
        getBrghnisses([1,2,3])
        bussy = False
        return brightnises[idx]



 


def change_brightness(id, value):
    new_brightness = str(float(find_brightnes(id)) + (value*10))
    logger.warning("find: "+str(float(find_brightnes(id))))
    logger.warning("id: "+str(id))

    logger.warning("value: "+str(value*10))
    logger.warning("value*10: "+str(value*10))
    logger.warning("ges: "+str(float(find_brightnes(id)) + (value*10)))
    #command = "sh /home/silas/.config/qtile/brightniss_control.sh "+str(id)+" "+new_brightness
    command = "ddcutil setvcp 10 "+new_brightness + "-d " +str(id+1)

    logger.warning("command: "+str(command))
    lazy.spawn(command)

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
