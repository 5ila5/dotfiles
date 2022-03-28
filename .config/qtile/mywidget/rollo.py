from requests import get, post
import os
import json
import sys

headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhMmM5NDMzMjhkNTI0MTA5OWNkNDQwMDIwZWJhODI1MiIsImlhdCI6MTYyODcwODgxNSwiZXhwIjoxOTQ0MDY4ODE1fQ.5WQzzNABOcGeazMBT8VLOtT-sk53a948XohquQ3gEtU",
           "content-type": "application/json",
            }


def activateBlendet():
    url = "http://eis.lan.home:8123/api/services/scene/turn_on"
    payload= {"entity_id": "scene.blendet"}
    post(url, headers=headers, json=payload)

def deactivateBlendet():
    url = "http://eis.lan.home:8123/api/services/cover/set_cover_position"
    payload= {"entity_id": "cover.fenster", "position": 100}
    response = post(url, headers=headers, json=payload)
    data = json.loads(response.text)

def setPosition(value):
    url = "http://eis.lan.home:8123/api/services/cover/set_cover_position"
    payload= {"entity_id": "cover.fenster", "position": value}
    response = post(url, headers=headers, json=payload)
    data = json.loads(response.text)

def getPosition():
    url = "http://eis.lan.home:8123/api/states/cover.fenster"
    payload= {"entity_id": "cover.fenster",}
    response = get(url, headers=headers, json=payload)
    data = json.loads(response.text)
    #print(data)
    if data == None or data == "" or data["attributes"]== None:
        return

    return data["attributes"]["current_position"]

def main():
    args = sys.argv
    if len(args) <2 :
        return
    
    if args[1] == "get":
        print(getPosition())
    elif args[1] == "set" and args[2].isnumeric():
        setPosition(int(args[2]))

    elif args[1] == "blendet":
        if getPosition() != 100:
            activateBlendet()

if __name__ == "__main__":
    main()


