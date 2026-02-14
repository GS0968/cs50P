import sys

if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments")

if ".py" in sys.argv[1]:
    filename=sys.argv[1]
    length=int(0)
    try:
        with open(filename) as file:
            lines=file.readlines()
        for line in lines:
            line=line.strip()
            if line.startswith("#") or line=="":
                pass
            else:
                length+=1
    except FileNotFoundError:
        sys.exit("File does not exist")
else:
    sys.exit("Not a Python file")

print(length)
