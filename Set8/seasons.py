from datetime import date
from datetime import timedelta
import sys
import inflect

class date_data:
    def __init__(self,givendate):
        self.gdate=givendate
        self._tdate=str(date.today())

    def checkdate(self):
        date.fromisoformat(self.gdate)

    def getdelta(self):
        date1=getdate(self.gdate)
        date2=getdate(self._tdate)
        delta=str(date2-date1)
        ddelta,tdelta=delta.split(" days, ")
        ddelta=int(ddelta)
        timediff=timedelta(days=ddelta)
        seconds=int(timediff.total_seconds())
        minutes=seconds//60
        return(convert(minutes))

def main():
    input_date=input("Date of Birth: ")
    process(input_date)

def process(input_date):
    x=date_data(input_date)
    try:
        x.checkdate()
    except ValueError:
        sys.exit("Invalid date")
    else:
        print(x.getdelta())

def getdate(s):
    year,month,day=s.split("-")
    year=int(year)
    month=int(month)
    day=int(day)
    return(date(year,month,day))

def convert(min):
    engine=inflect.engine()
    x=engine.number_to_words(min)
    v=x.split(" ")
    i=0
    tstring=str()
    while i!=len(v):
        z=v[i]
        if z!="and":
            tstring=tstring+z+" "
        i+=1
    tstring=tstring+"minutes"
    return tstring.capitalize()

if __name__ == "__main__":
    main()
