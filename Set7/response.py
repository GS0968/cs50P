import validators


email=input("Email address: ")
if validators.email(email):
    print("Valid")
else:
    print("Invalid")
