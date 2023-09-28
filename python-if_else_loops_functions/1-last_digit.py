#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    number *= -1
u = number % 10
str = "Last digit of "
if (u > 5):
    print(f"{str}{number} is {u} and is greater than 5")
elif (u == 0):
    print(f"{str}{number} is {u} and is 0")
else:
    print(f"{str}{number} is {u} and is less than 6 and not 0")
