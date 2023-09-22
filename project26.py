# Project 26 : Hangman 
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


import random

print("Welcome to hangman !")

words = ["harshita", "guru prasad", "barath"]
word = random.choice(words)
word_len = len(word)
clues= '_'*word_len

timmer = 0
word_guess=input("Enter The word you want to guess")
word_list=[]
for i in word:
    word_list.append(i)
word_guessed=[]
while True:
    word_let=input("Enter the guess word")
    if word_guess in word_list and word_let not in word_guessed:
        print ("The guess is correct")
        
        

for i in word : 
    if i=" ":
        print("   ", end = "")
        continue
    print("_", end=" ")
    

