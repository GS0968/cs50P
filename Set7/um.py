import re

def main():
    print(count(input("Text: ")))

def count(s):
    matches=re.findall(r'\b(um+|Um)',s)
    print(matches)
    i=int(0)
    counter=int(0)
    while i!=len(matches):
        look=matches[i]
        print(look)
        if re.search(r"^um$",look) or re.search(r"^Um$",look):
            counter+=1
        i+=1
    return counter

if __name__=="__main__":
    main()
