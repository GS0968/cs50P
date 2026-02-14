def main():
    plate= input("Plate: ")
    if is_valid(plate)== "Valid":
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    alphacounter= int(0)
    intcounter= int(0)
    wrongcounter= int(0)
    if s.isalpha()==True:
        if 6>=len(s)>=2:
            return("Valid")
        else:
            return("Invalid")
    elif s.isalnum()== True:
        for i in s:
            if intcounter==0 and i.isalpha()==True:
                alphacounter+= 1
            elif alphacounter>=2 and i.isdigit()== True:
                if i=="0" and intcounter==0:
                    wrongcounter+= 1
                else:
                    intcounter+= 1
            elif intcounter > 0 and i.isalpha()==True:
                wrongcounter+= 1

        totalcounter=int(intcounter+alphacounter)
        if 6>=totalcounter>=2 and wrongcounter== 0:
            return("Valid")
        else:
            return("Invalid")
    else:
        return("Invalid")
main()
