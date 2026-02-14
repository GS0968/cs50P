import tabulate
import sys

if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
if ".csv" in sys.argv[1]:
    table=[]
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                type,small,large=line.strip().split(",")
                row={"type":type,"small":small,"large":large}
                table.append(row)
        print(tabulate.tabulate(table, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File doesn't exist")
else:
    sys.exit("Not a CSV file")
