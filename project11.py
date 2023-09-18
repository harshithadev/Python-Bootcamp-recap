# Project 11 : Leap year code, with functions. 
def calculate_leap_year(year):
    if year % 4 == 0 : 
        if year % 100 == 0 : 
            if year % 400 == 0: 
                print ("Leap year !!!")
            else : 
                print("Not Leap year !!!")
        else : 
            print("Leap year !!")
    else : 
        print("Not Leap year !")


year = int(input("Enter a year : "))
calculate_leap_year(year)


