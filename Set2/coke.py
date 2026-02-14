Amount_due= int(50)
print("Amount due:", Amount_due)
while Amount_due>= 1:
    CoinInsert= int(input("Insert Coin: "))
    if CoinInsert== 50 or CoinInsert== 25 or CoinInsert== 10 or CoinInsert== 5:
        Amount_due= Amount_due-CoinInsert
    if Amount_due>= 1:
        print("Amount due:",Amount_due)

ChangeOwe= Amount_due
if ChangeOwe < 0:
    ChangeOwe=ChangeOwe*-1
    print("Change Owed:",ChangeOwe)
else:
    print ("Change Owed: 0")
