def main():
    input_time = input("Enter the time in 24 hour format: ")
    converted_time = convert(input_time.strip())
    print(meal(float(converted_time)))

def convert(input_time):
    hourconvertstr, minuteconvertstr = input_time.split(':')
    minuteconvert = float(minuteconvertstr) / 60
    hourconvert = int(hourconvertstr)
    time_float = (hourconvert + minuteconvert)
    return str(time_float)

def meal(time_float):
    type_of_meal = ""

    if 7<=time_float<=8:
        type_of_meal = "breakfast time"
    elif 12<=time_float<=13:
        type_of_meal = "lunch time"
    elif 18<=time_float<=19:
        type_of_meal = "dinner time"
    else:
        type_of_meal = ""
    return type_of_meal

if __name__ == "__main__":
    main()
