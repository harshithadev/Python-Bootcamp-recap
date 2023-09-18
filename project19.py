# Project 19 : Rock paper and sciscors. 
import random

def decision(user_choice, computer_choice) : 
    """Result of user's and computer's choice."""
    if user_choice == computer_choice :
        print("Draw !")
    elif user_choice == 'rock' :
        if computer_choice == 'sciscors' :
            print("You WIN !")
        else : 
            print("You LOSE !")
    elif user_choice == 'paper' :
        if computer_choice == 'sciscors' :
            print("You LOSE !")
        else : 
            print("You WIN !")
    else : # your choice is sciscors
        if computer_choice == 'rock' :
            print("You LOSE !")
        else : 
            print("You WIN !")  

def generate_computer_choice():
    """Generates a randomized choice output for the computer"""
    choices = ['rock', 'paper', 'sciscors']
    return random.choice(choices)

contin = 'y'
while contin == 'y' :
    print("rock paper or sciscors ? ")
    user_choice = input("Your choice : ")
    # can make sure the user enters either of three choices else error ! 
    computer_choice = generate_computer_choice()
    print(f"Computer's choice : {computer_choice}")
    decision(user_choice, computer_choice)
    contin = input("Wanna play again ? (y/n) ...")

print("\nHave a good day :)")