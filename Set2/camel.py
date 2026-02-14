Camelcase= input("camelCase: ")
for i in Camelcase:
    if i.isupper()==True:
        i= "_"+i.lower()
    print(i, end="")
