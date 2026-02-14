Name= []
count=0
while True:
    try:
        InputName=input("Name: ")
    except EOFError:
        print()
        break
    else:
        Name.append(InputName)
        count+=1

OutputMsg=str()
u=int(1)
for counter in Name:
    if u==1:
        OutputMsg= ("Adieu, adieu, to "+counter)
        u=u+1
    elif u==len(Name) and u==2:
        OutputMsg= (OutputMsg+" and "+counter)
    elif u==len(Name):
        OutputMsg= (OutputMsg+", and "+counter)
    else:
        OutputMsg= (OutputMsg+", "+counter)
        u=u+1

print(OutputMsg)
