#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = 0

if number >= 0:
    lastDigit = number % 10
else:
    lastDigit = (-number % 10) * -1

result = f"Last digit of {number} is {lastDigit}"

if lastDigit > 5:
    print(f"{result} and is greater than 5")
elif lastDigit == 0:
    print(f"{result} and is 0")
else:
    print(f"{result} and is less than 6 and not 0")
