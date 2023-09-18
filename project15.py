# Project 15 : Dice Rolling 
import random

def generate_dice_output():
    print(f"Dice 1 says : {random.randint(1,6)}")
    print(f"Dice 2 says : {random.randint(1,6)}")

more = "yes"
while more == "yes" : 
    generate_dice_output()
    more = input("want to continue ? (yes/no) ")
print("Have a good day :)")