import sys
import pyfiglet

while True:
    if len(sys.argv)>1:
        if sys.argv[1]=="-f" or sys.argv[1]=="--format":
            break
        else:
            sys.exit("Invalid first command-line argument")
    else:
        break

i= str(input("Input: "))
f=str()
if len(i)==0:
    sys.exit()
else:
    if len(sys.argv)>1:
        f= pyfiglet.figlet_format(i, font=str(sys.argv[2]))
    else:
        f=pyfiglet.figlet_format(i)
print (f)
