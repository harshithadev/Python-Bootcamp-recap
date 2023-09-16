# Project 5 ; Trip Cost calculator 

print("Hello User !")
print("The total cost of your trip is " + \
    str( float(input("Enter the number of days of your trip : ")) *\
        float(input("Enter the price of hotel per night : ")) +\
            float(input("Enter the cost of the flight tickets : ")) +\
                float(input("Enter the cost of car rentals : ")) +\
                    float(input("Enter the cost of other expenses: ")) ))