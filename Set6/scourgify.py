import sys
import csv
def main():
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")

    if ".csv" in sys.argv[1]:
        studentinfo=get_file(sys.argv[1])
    else:
        sys.exit("Not a CSV file")
    if ".csv" in sys.argv[2]:
        write_file(sys.argv[2], studentinfo)
    else:
        sys.exit("not a CSV file")


def get_file(filename):
    students=[]
    try:
        with open(filename) as file:
            reader=csv.DictReader(file)
            for line in reader:
                students.append({"name": line["name"], "house":line["house"]})
        return students
    except FileNotFoundError:
        sys.exit(f"Could not read {filename}")


def write_file(filename, table):
    students=table
    with open(filename, "w") as file:
        file.write("first,last,house\n")
        for i in students:
            lastname,firstname=str(i['name']).split(", ")
            house=str(i['house'])
            file.write(f"{firstname},{lastname},{house}\n")

if __name__=="__main__":
    main()
