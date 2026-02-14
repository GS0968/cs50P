import re

def main():
    time=input("Hours: ")
    print(convert(time))


def convert(s):
    time=gettime(s)
    if checktime(time)=="True":
        return time
 

def gettime(u):
    AMhour=["01","02","03","04","05","06","07","08","09","10","11","00"]
    time1,time2=u.split(" to ")
    #formatting the first time
    if time1.count(":")==1:
        hour1,rest=time1.split(":")
        minute1,period1=rest.split(" ")
    else:
        hour1,period1=time1.split(" ")
        minute1="00"
    if period1=="AM":
        hour1=int(hour1)-1
        time1=AMhour[hour1]+":"+minute1
    elif period1=="PM":
        if hour1=="12":
            time1=str(hour1)+":"+minute1
        else:
            hour1=int(hour1)+12
            time1=str(hour1)+":"+minute1

    #formatting the second time
    if time2.count(":")==1:
        hour2,rest2=time2.split(":")
        minute2,period2=rest2.split(" ")
    else:
        hour2,period2=time2.split(" ")
        minute2="00"
    if period2=="AM":
        hour2=int(hour2)-1
        time2=AMhour[hour2]+":"+minute2
    elif period2=="PM":
        if hour2=="12":
            time2=str(hour2)+":"+minute2
        else:
            hour2=int(hour2)+12
            time2=str(hour2)+":"+minute2
    #concatinating them together
    time=time1+" to "+time2
    return time


def checktime(s):
    if re.search(r"^0[0-9]:[0-5][0-9] to 0[0-9]:[0-5][0-9]$",s) or re.search(r"^0[0-9]:[0-5][0-9] to 1[0-9]:[0-5][0-9]$",s) or re.search(r"^0[0-9]:[0-5][0-9] to 2[0-3]:[0-5][0-9]$",s) or re.search(r"^1[0-9]:[0-5][0-9] to 0[0-9]:[0-5][0-9]$",s) or re.search(r"^1[0-9]:[0-5][0-9] to 1[0-9]:[0-5][0-9]$",s) or re.search(r"^1[0-9]:[0-5][0-9] to 2[0-9]:[0-5][0-9]$",s) or re.search(r"^2[0-9]:[0-5][0-9] to 0[0-9]:[0-5][0-9]$",s) or re.search(r"^2[0-9]:[0-5][0-9] to 1[0-9]:[0-5][0-9]$",s) or re.search(r"^2[0-3]:[0-5][0-9] to 2[0-3]:[0-5][0-9]$",s):
        return "True"
    else:
        raise ValueError




if __name__ == "__main__":
    main()

#ez only
