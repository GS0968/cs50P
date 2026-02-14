def main():
    while True:
        fraction= input("Fraction: ")
        try:
            percentage= convert(fraction)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break
    print(gauge(percentage))

def convert(fraction):
    try:
        num1, num2 =fraction.split("/")
        num1=int(num1)
        num2=int(num2)
    except ValueError:
        raise ValueError
    else:
        try:
            out= (num1/num2)*100
            out= round(out)
        except ZeroDivisionError:
            raise ZeroDivisionError
        else:
            if 100>=out>=0:
                return out
            else:
                raise ValueError

def gauge(percentage):
    if percentage==100 or percentage==99:
        return "F"
    elif percentage==0 or percentage==1:
        return "E"
    else:
        return f"{percentage}%"

if __name__=="__main__":
    main()
