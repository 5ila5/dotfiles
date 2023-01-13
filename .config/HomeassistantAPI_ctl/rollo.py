from requests import get, post
import os
import json
from apiAuth import headers
import sys, getopt

base_url = 'http://eis.lan.home:8123/api/'
entity_id_tuer = 'cover.tuer_turfenster'
entity_id_fenster = 'cover.fenster'


def activateBlendet():
    url = base_url+"services/scene/turn_on"
    payload= {"entity_id": "scene.blendet"}
    post(url, headers=headers, json=payload)


def setRollo(entity_id,pos):
    url = base_url+ "services/cover/set_cover_position"
    payload= {"entity_id": entity_id, "position": pos}
    response = post(url, headers=headers, json=payload)
    #print(response.text)
    
    data = json.loads(response.text)
    #print(data)

def setTuer(pos):
    setRollo(entity_id_tuer,pos)

def setFenster(pos):
    setRollo(entity_id_fenster ,pos)

def deactivateBlendet():
    setTuer(100)

def get_tuer() -> int:
    url=base_url+  f"states/{entity_id_tuer}"
    response = get(url, headers=headers)
    
    data = json.loads(response.text)
    if "attributes" in data and "current_position" in data["attributes"]:
        return int(data["attributes"]["current_position"])
    return 400

def get_fenster() -> int:
    url=base_url+  f"states/{entity_id_fenster}"
    response = get(url, headers=headers)
    
    data = json.loads(response.text)
    if "attributes" in data and "current_position" in data["attributes"]:
        return int(data["attributes"]["current_position"])
    return 400
        








def main():
    opts, args = getopt.getopt(sys.argv[1:], "t:f:tf:ft:d", ["tuer =","fenster =","beide ="])
    if "-d" in opts:
        print(f"sys.argv[1:]: {sys.argv[1:]}")
        print(f"opts: {opts}")
        print(f"args: {args}")

    
    if opts == [] and args == []:
        activateBlendet()
        return

    if len(args)>0 and "get" == args[0]:
        if args[1] == "fenster":
            print(get_fenster())
            return

        if args[1] == "tuer":
            print(get_tuer())
            return

        if opts == []:
            print(f"[{get_tuer()},{get_fenster()}]")
            return
        
        


    for opt in opts:
        print(f"opt: {opt}")

        if ("-f" == opt[0] or "--fenster" in opt[0]or "--beide" in opt[0]) and opt[1].isdigit():
            pos = int(opt[1])
            if pos <= 100 and pos >= 0:
                setFenster(pos)
                print("setFenster("+str(pos)+")")
            else:
                print("position is not a digit")
        if ("-t" == opt[0] or "--tuer" in opt[0] or "--beide" in opt[0]) and opt[1].isdigit():
            pos = int(opt[1])
            if pos <= 100 and pos >= 0:
                print("setTuer("+str(pos)+")")
                setTuer(pos)
            else:
                print("position is not a digit")
        else:
            print("("+str("-t" == opt[0])+ " or " +str("--tuer" == opt[0]) +" or "+ str("--beide" == opt[0])+ ") and " +str(opt[1].isdigit()))

    

if __name__ == "__main__":
    main()
