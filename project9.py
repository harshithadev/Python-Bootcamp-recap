# Project 9 : Gross pay with exception tweak. 

try : 
    hours = float(input("Enter the number of hours you work : "))
    rate = float(input("Enter the rate per hour : "))
except ValueError:
    print("Invalid input : not a number!")   
else :
    if hours > 40:
        rate *= 1.4
    salary = hours * rate
    print(f"Your gross salary is : {round(salary,3)}")
finally :
    print("Have a good day !")