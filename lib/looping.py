#!/usr/bin/env python3

def happy_new_year():
    i = 11  
    while i > 0 :
        i = i - 1
        print(i)
    print("Happy New Year!")

def square_integers(int_list):
    square_list = []
    for x in int_list:
        square_list.append(x **2)
    return square_list    
    

def fizzbuzz():
    
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
           print("FizzBuzz")
        elif num % 3 == 0:
           print("Fizz")
        elif num % 5 == 0:
           print("Buzz")
        else:
           print(num)   
               

