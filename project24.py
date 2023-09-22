# Project 24 : Ceasar Cipher 

import string

alphas = string.ascii_lowercase
n = int(input("Enter secret number : "))
cipher = [alphas[(i+n)%26] for i in range(len(alphas))]
print(f'New secret message is :{"".join([cipher[alphas.index(s)] for s in input("Enter your secret message : ")])}')

