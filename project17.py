# Project 17 : Guessing the number
import random 

def generate_guess(a,b):
    return random.randint(a,b)

def guess_answer(n, guess):
    if guess > n : 
        print("Your guess is too HIGH!")
    elif guess < n :
        print("Your guess is too LOW!")
    else : 
        print("CONGRADULATIONS!! you are right!")
        return 1
    return 0

a,b = map(int, input("Enter range to guess a number in (seperated by space) : ").split(" "))
n = generate_guess(a,b)
correct = 0
for i in range (3):
    correct = guess_answer(n, int(input(f"Enter guess no {i+1} : ")))
    if correct == 1 : 
        break 
if correct == 0 : 
    print("Too bad, you are out of guesses!")
print("Have a goood day :)")
    
