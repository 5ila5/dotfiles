from shutil import copyfile

copyfile("config.py","config.old.py")
with open("config.py","w") as new:
    with open("configWIP.py","r") as wip:
            new.write(wip.read().replace("mod = \"mod1\"","mod = \"mod4\""))
