#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
str = "Last digit of"
if (last_digit > 5):
    print(f"{str} {number} is {last_digit} and is greater than 5")
elif (0 < last_digit < 6):
    print(f"{str} {number} is {last_digit} and is less than 6 and not 0")
else:
    print(f"{str} {number} is {last_digit} and is 0")