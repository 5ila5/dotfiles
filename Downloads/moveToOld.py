#!/usr/bin/python
import os
import datetime


def main():
    curr_folder= os.path.dirname(os.path.realpath(__file__))+"/"
    this_script_file = __file__.split("/")[-1]
    files = os.listdir(curr_folder)
    
    if this_script_file in files:
        files.remove(this_script_file)
    if "old" in files:
        files.remove("old")
    if not os.path.exists(curr_folder+"old"):
        os.mkdir(curr_folder+"old")


    for file in files:
        mod_date = datetime.datetime.fromtimestamp(os.path.getmtime(curr_folder+file))
        diffrence = datetime.datetime.now() - mod_date
        if diffrence.days > 7:
            os.rename(curr_folder+file,curr_folder+"old/"+file)

if __name__ == "__main__":
    main()