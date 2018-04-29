import datetime
def show_header():
    print("---------------------------------------------------------------------------------------------------")
    print("                                     DISTANCE TO BIRTHDAY")
    print("---------------------------------------------------------------------------------------------------")
    print(" ")

def get_birthday():
    uname= input("O Charming, and what must thy name be?")
    print("Hi {}, let us compute how close are you to your nearest birthday!!".format(uname))
    year= int(input("Year [YYYY]="))
    month= int(input("month [MM]="))
    day= int(input("day [DD]="))
    birthday= datetime.date(year, month, day)
    return birthday

def compute_day_distance(fday, iday):
    mrbday= datetime.date(year=iday.year, month= fday.month, day= fday.day)
    dt= mrbday-iday
    return dt.days

def show_message(ddist):
    if ddist<0:
        print("Your birthday was {0} days ago!".format(abs(ddist)))
    elif ddist>0:
        print("Your birthday is in {0} days".format(ddist))
    else:
        print("Wish you many happy returns of the day!!")

def main():
    show_header()
    bday= get_birthday()
    today= datetime.date.today()
    day_distance= compute_day_distance(bday, today)
    show_message(day_distance)

main()