while True:
    fraction= input("Fraction: ")
    try:
        num1, num2= fraction.split("/")
        num1= int(num1)
        num2= int(num2)
    except ValueError:
        pass
    else:
        try:
            out= (num1/num2)*100
            out= round(out)
        except ZeroDivisionError:
            pass
        else:
            if 100>=out>=0:
                break

if out==100 or out==99:
    print ("F")
elif out==0 or out==1:
    print("E")
else:
    print (f"{out}%")
