# Project 10 : Score Checker 
try :    
    score = float(input("Enter the score between 0 to 1 : "))
    if score < 0 or score > 1:
        raise Exception() 
except ValueError:
    print("Error : Entry is not a numerical! ")
except : 
    print("Error : Number not in range! ")
else : 
    # lasy to write too many conditions, let's keep it simple. 
    if score < 0.5 : 
        print("Bad Score !")
    else : 
        print("Good Score !")
finally:
    print("Have a good day :) ")
