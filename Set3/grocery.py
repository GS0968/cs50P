#itemlist={}
#orderlist={}
def main():
    inputlist = getlist()
    inputlist.sort()
    count = getcount(inputlist)
    for vegetable in count:
        print(count[vegetable], vegetable)

def getcount(inputlist):
    countlist = {}
    for  vegetable in inputlist:
        if vegetable in countlist:
            countlist[vegetable] = countlist[vegetable]+1
        else:
            countlist[vegetable] = 1

    return countlist


def getlist():
    #i= int(0)
    itemlist=[]
    while True:
        try:
            item= input()
        except EOFError:
            break
        else:
            itemlist.append(item.upper())
    return itemlist

main()
