# Project 7 : Leap year calculator.

year = int(input("Enter a year : "))
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


# # Interesting tweak to an otherwise mundane problem : Find the next leap year, given an year.
    
# year = int(input("Enter an year : "))
# if year % 4 == 0 : 
#     year += 4 
#     if year % 100 == 0 : 
#         if year % 400 == 0: 
#             print(f"The next leap year is : {year}")
#         else : 
#             print(f"The next leap year is : {year+4}")
#     else : 
#         print(f"The next leap year is : {year}")
        
# else : 
#     print(f"The next leap year is : {year+(4-(year%4))}")