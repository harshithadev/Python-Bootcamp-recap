# Project 22 : Find the gold 
import random

m, n = map(int, input("Enter a m*n map to choose from (seperated by space) : ").split(" "))
#print(m,n)
star_map = [[0 for i in range(n)] for i in range(m)]
star_x, star_y = random.randint(0,m-1), random.randint(0,n-1)
# print(star_map)
star_map[star_x][star_y] = 'G'
print(star_x, star_y)
# print(star_map)
guess_x, guess_y = map(int, input("Enter your guess x and y coordinates (seperated by space) : ").split(" "))

if guess_x == star_x and guess_y == star_y :
    print("Your guess is right !!!!!")
else : 
    print("Sorry, better luck next time ! ")
# print(star_map)
for row in star_map:
    for unit in row : 
        print(f"{unit} ", end="")
    print()
#print(star_x, star_y)
#print(star_map)
