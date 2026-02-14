def main():
    Inputtxt= input("Input: ")
    print(shorten(Inputtxt))

def shorten(word):
    value= str()
    for i in word:
        match i:
            case "a"|"A":
                i= ""
            case "e"|"E":
                i= ""
            case "i" | "I":
                    i= ""
            case "o" | "O":
                    i= ""
            case "u" | "U":
                    i= ""
            case "_":
                  i=i
        value= value+i
    return value

if __name__=="__main__":
    main()
