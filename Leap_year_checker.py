#basic and simple leap year checker

def leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print("It's a leap year")
            else:
                print("Not a leap year")
        else:
            print("It's a leap year")
    else:
        print("Not a leap year")

year=int(input("Enter the year : "))
leap_year(year)