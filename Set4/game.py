import random

while True:
    try:
        maxdigit= int(input("Level: "))
    except ValueError:
        pass
    else:
        break
answer= random.randint(1, maxdigit)
while True:
    try:
        guess= int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess<1:
            pass
        elif guess==answer:
            print("Just right!")
            break
        elif guess>answer:
            print("Too large!")
        elif guess<answer:
            print("Too small!")

