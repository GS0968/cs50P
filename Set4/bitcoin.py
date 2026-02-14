import requests
import sys
while True:
    if len(sys.argv)<2:
        sys.exit("missing command line argument")
    try:
        numofcoins=float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:
        bitcoininfo= requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=06d4d1728ac705d7329f9ffedbeff72a939cdb4e8fdb0c0f22411df2856a5d12")
        o=bitcoininfo.json()
        bitcoindata=o['data']
        bitcoinprice=float(bitcoindata['priceUsd'])
        output=float(bitcoinprice*numofcoins)
        outputformated= float(f"{output:.4f}")
        outputformated= f"{outputformated:,}"
        print (f"${outputformated}")
        break
