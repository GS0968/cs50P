def main():
    Greeting= input("Enter your greeting: ").strip()
    print(f"${value(Greeting)}")

def value(greeting):
    greeting=str(greeting).lower()
    if greeting.find('h') != -1 and greeting.find("hello") != -1:
        return(0)
    elif greeting.find('h') != -1 and greeting.find("hello") == -1:
        return(20)
    else:
        return(100)

if __name__=="__main__":
    main()
