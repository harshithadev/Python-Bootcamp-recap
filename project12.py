# Project 12 : Gross pay with functions. 

def check_if_number(num):
    """Checks if number, returns converted datatype. Else raises exception."""
    try : 
        num = float(num)
    except ValueError:
        print("Not a numerical ! ")
        quit()
    else : 
        return num
    
def calculate_salary(hours, rate):
    """Returns salary based on hours and rate"""
    if hours > 40:
        rate *= 1.4
    return hours * rate

hours = input("Enter the number of hours you work : ")
hours = check_if_number(hours)
rate = input("Enter the rate per hour : ")
rate = check_if_number(rate)

salary = calculate_salary(hours, rate)
print(f"Your gross salary is : {round(salary,3)}")
print("Have a good day !")