def main ():
    dollars= dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage tip would you like to give? "))
    tip = dollars * percent/100
    print(f"Leave ${tip:.2f} tip.")

def dollars_to_float(d):
    """Convert a string representing dollars to a float."""
    return float(d.replace("$", ""))
def percent_to_float(p):
    """Convert a string representing dollars to a float."""
    return float(p.replace("%", ""))
main()
