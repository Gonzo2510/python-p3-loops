#!/usr/bin/env python3

def happy_new_year():
    x = 10
    while x > 0:
        print(x)
        x-=1
    print('Happy New Year!')

def square_integers(int_list):
    my_list=[]
    for i in int_list:
        square = i*i
        my_list.append(square)
    return my_list

def fizzbuzz():
    x = 1
    while x <= 100:
        if x % 3 == 0 and x % 5 == 0:
            print('FizzBuzz')
        elif x % 3 == 0:
            print('Fizz')
        elif x % 5 == 0:
            print('Buzz')
        else: 
            print(x)
        x+=1

fizzbuzz()