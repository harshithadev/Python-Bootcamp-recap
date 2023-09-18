# Project 6 : Gross Calculator with overpay feature.

hours = float(input("Enter the number of hours you work : "))
rate = float(input("Enter the rate per hour : "))
if hours > 40:
    rate *= 1.4
salary = hours * rate
print(f"Your gross salary is : {round(salary,3)}")