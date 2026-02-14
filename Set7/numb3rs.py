import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    ip=ip.strip()
    ipnum=[]
    bool=True
    try:
        a,b,c,d=ip.split(".")
        ipnum.append(a)
        ipnum.append(b)
        ipnum.append(c)
        ipnum.append(d)
        for i in range(0,4):
            u=ipnum[i]
            print(u)
            match len(u):
                case 1:
                    if re.search("^[0-9]$",u):
                        pass
                    else:
                        bool=False
                case 2:
                    if re.search("^[1-9][0-9]$",u):
                        pass
                    else:
                        bool=False
                case 3:
                    if re.search("^[1][0-9][0-9]$",u) or re.search("^[2][0-4][0-9]$",u) or re.search("^[2][5][0-5]$",u):
                        pass
                    else:
                        bool=False
                case _:
                    bool=False
        return bool
    except ValueError:
        return "False"
if __name__=="__main__":
    main()
