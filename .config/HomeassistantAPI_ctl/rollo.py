from requests import get, post
import os
import json
from apiAuth import headers
import sys, getopt

def activateBlendet():
    url = "http://eis.lan.home:8123/api/services/scene/turn_on"
    payload= {"entity_id": "scene.blendet"}
    post(url, headers=headers, json=payload)


def setRollo(entity_id,pos):
    url = "http://eis.lan.home:8123/api/services/cover/set_cover_position"
    payload= {"entity_id": entity_id, "position": pos}
    response = post(url, headers=headers, json=payload)
    #print(response.text)
    
    data = json.loads(response.text)
    #print(data)

def setTuer(pos):
    setRollo("cover.shellyswitch1",pos)

def setFenster(pos):
    setRollo("cover.fenster",pos)

def deactivateBlendet():
    setTuer(100)






def main():
    opts, args = getopt.getopt(sys.argv[1:], "t:f:", ["tuer =","fenster ="])
    
    
    if opts == []:
        activateBlendet()
        return

    for opt in opts:
        #iprint(opt)
        if ("-f" == opt[0] or "--fenster" == opt[0]) and opt[1].isdigit():
            pos = int(opt[1])
            if pos <= 100 and pos >= 0:
                setFenster(pos)
                print("setFenster("+str(pos)+")")
            else:
                print("position is not a digit")
        if ("-t" == opt[0] or "--tuer" == opt[0]) and opt[1].isdigit():
            pos = int(opt[1])
            if pos <= 100 and pos >= 0:
                print("setTuer("+str(pos)+")")
                setTuer(pos)
            else:
                print("position is not a digit")



if __name__ == "__main__":
    main()
