enter= input("enter the expression: ").strip()
def separateexp(enter): return x,z,y
if '+' in enter:
    x, z = enter.split('+')
    y= "+"
elif '-' in enter:
    x, z = enter.split('-')
    y= "-"
elif '*' in enter:
    x, z = enter.split('*')
    y= "*"
elif '/' in enter:
    x, z = enter.split('/')
    y= "/"
output =float()
match y:
    case "+":
        output = float(x) + float(z)
    case "-":
        output = float(x) - float(z)
    case "*":
        output = float(x) * float(z)
    case "/":
        output = float(x) / float(z)

print (output)

