from PIL import Image
from PIL import ImageOps
import sys

if len(sys.argv)<3:
    sys.exit("Too few comand-line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
name1,type1=str(sys.argv[1]).split(".")
name2,type2=str(sys.argv[2]).split(".")
if type1!=type2:
    sys.exit("input and output have different extensions")
try:
    person= Image.open(sys.argv[1])
    shirt= Image.open("shirt.png")
    shirt=shirt.convert("RGBA")
    size=shirt.size
    person=ImageOps.fit(person,size)
    person.paste(shirt,(0,0),shirt)
    person.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("could not find image file")
