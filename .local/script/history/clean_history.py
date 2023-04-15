#!/usr/bin/python

FILE = "/home/silas/.bash_eternal_history"

lines = []

def main():
    c=0
    with open(FILE, "r", encoding="utf-8") as f:
        for line in reversed(list(f)):
            c+=1
            if line not in lines:
                lines.append(line)
            if not c %1000:
                print(f"{c} lines processed")
                
    with open(f"{FILE}", "w", encoding="utf-8") as f:
        f.writelines(reversed(lines))
    
                

if __name__ == "__main__":
    main()