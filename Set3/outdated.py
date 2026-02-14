monthlist= [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]
while True:
    inputdate= str(input("Date: "))
    #if the inputdate is starting with string
    for i in range (0, len(monthlist)):
        if inputdate.startswith(monthlist[i])==True:
            bool= True
            break
    if bool==True:
        if inputdate.count(",")>0:
            rest,year= inputdate.split(',')
            month,day= rest.split(' ')
            month=str(i+1)
        try:
            if inputdate.count('/')>0 or int(day)>31:
                pass
            else:
                break
        except NameError:
            pass
    else:
        if "/" in inputdate:
            month,day,year=inputdate.split('/')
            if int(day)>31 or int(month)>12 :
                pass
            else:
                try:
                    int(month)
                except ValueError:
                    pass
                else:
                    break
        else:
            pass
year=year.strip()
day=day.strip()
month=month.strip()
if int(month)<10:
    month=str(month)
    month="0"+month
if int(day)<10:
    day="0"+day
out=str(f"{year}-{month}-{day}")
print(out)
