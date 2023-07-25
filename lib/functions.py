#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")
greet("Naureen")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
greet_with_default()
greet_with_default("Sunny")

def add(num1, num2):
    result = num1 + num2
    print (result)
    # return result
num1 = 1
num2 = 2
add(num1,num2)


def halve(number):
    result = number / 2
    print(result)
number = 4
halve(4)




