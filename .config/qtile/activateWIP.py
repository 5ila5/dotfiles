from shutil import copyfile


def main():
    with open("relevantConfigFiles.csv","r") as f:
        for toCopy in f.read().replace("\n","").replace(" ","").split(","):
            copyfile(toCopy,"../"+toCopy)


if __name__ == "__main__":
    main()


