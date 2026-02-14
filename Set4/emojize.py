import emoji

Inputtxt= input("Input: ")
if "earth" in Inputtxt:
    print(emoji.emojize(Inputtxt, language='alias'))
else:
    if '_' in Inputtxt:
        print(emoji.emojize(Inputtxt))
    else:
            print(emoji.emojize(Inputtxt, language='alias'))
