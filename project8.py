# Project 8 : LOVE calculator. (side comment XD)

first_name = input("Enter the first name : ")
second_name = input("Enter the second name : ")
name = first_name + second_name # coz we dont really need them seperately. 

true_counter = 0
love_counter = 0
for c in name : 
    if c in 'true':
        true_counter += 1
        #print(f"true : {c} present {name.count(c)} times... ")
    if c in 'love':
        love_counter += 1
        #print(f"love : {c} present {name.count(c)} times... ")

print(f"Your love score is : {true_counter}{love_counter}")
        
