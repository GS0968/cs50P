import random


def main():
    level=get_level()
    counter=int(1)
    wrongq= int(0)
    while counter<10:
        x= generate_integer(level)
        y= generate_integer(level)
        sum= x+y
        wrong=int(0)
        while True:
            inputmsg= input(f"{x} + {y} =")
            if inputmsg==str(sum):
                counter+=1
                if wrong!=0:
                    break
            elif wrong==2:
                print("EEE")
                print(f"{x} + {y} = {sum}")
                counter+=1
                wrongq+=1
                break
            else:
                print("EEE")
                wrong+=1
    score= counter-wrongq
    print (f"Score: {score}")

def get_level():
    while True:
        try:
            level= int(input("Level: "))
        except ValueError:
            pass
        else:
            if 0<level<4:
                break
            else:
                pass
    return level

def generate_integer(level):
    if level==1:
        x= random.randint(0,9)
    elif level==2:
        x= random.randint(10,99)
    elif level==3:
        x= random.randint(100,999)
    return x

if __name__=="__main__":
    main()
