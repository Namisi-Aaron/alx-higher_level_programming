#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def is_positive(number):
    if number > 0:
        return True
    else:
        return False


def is_greater(num):
    if num > 5:
        return True
    else:
        return False


sign = is_positive(number)
num = abs(number) % 10

if num == 0:
    print(f"Last digit of {number} is {num} and is 0")
elif sign is True:
    if is_greater(num):
        print(f"Last digit of {number} is {num} and is greater than 5")
    else:
        print(f"Last digit of {number} is {num} and is less than 6 and not 0")
else:
    num *= -1
    if is_greater(num):
        print(f"Last digit of {number} is {num} and is greater than 5")
    else:
        print(f"Last digit of {number} is {num} and is less than 6 and not 0")
