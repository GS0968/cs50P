Greeting= input("Enter your greeting: ").strip()
if Greeting.find('H') != -1 and Greeting.find("Hello") != -1:
    print("$0")
elif Greeting.find('H') != -1 and Greeting.find("Hello") == -1:
    print("$20")
else:
    print("$100")
