# Project 18 : password generator.

import random 
import string

alphabets = list(string.ascii_lowercase)
numbers = list(map(str, range(9)))
symbols = list("!@#$%^&*()_-+=/?")

a = int(input("Enter the number of alphabets desired : "))
n = int(input("Enter the number of numbers desired : "))
s = int(input("Enter the number of symbols desired : "))

password = random.choices(alphabets, k = a) + random.choices(numbers, k = n) + random.choices(symbols, k = s)
password = "".join(random.sample(password, k=len(password)))
print(f"Your password is : {password}")