# Project 13 : Cold, warm or Hot.

def find_temp(temp):
    """Returns type of temperature."""
    if temp < 18 :
        return "COLD"
    elif temp < 30 :
        return "MEDIUM"
    else : 
        return "HOT"
    
temp = int(input("Enter a current temperature : "))
print(f"The temperature is {find_temp(temp)} !")
