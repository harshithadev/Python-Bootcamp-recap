# Project 16 : Fizz Buzz 

def fizz_buzz(n):
    for i in range(1,n+1):
        if i%5 == 0 and i%7 == 0 : 
            print("Fizz Buzz")
        elif i%5 == 0 : 
            print("Fizz")
        elif i%7 == 0 : 
            print("Buzz")
        else : 
            print(i)
            
n = int(input("Enter a number till which you wanna play : "))
fizz_buzz(n)
