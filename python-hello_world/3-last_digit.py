#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

def last_num(number):
    return abs(number) % 10

if number > 0:
    last_digit = last_num(number)
    if last_digit > 5:
        print("Last digit of {} is {} and is greater than 5".format(number, last_digit))
    elif last_digit == 0:
        print("Last digit of {} is 0 and is 0".format(number))
    elif last_digit < 6 and last_digit != 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_digit))

elif number < 0:
    last_digit = last_num(number)
    if last_digit == 0:
        print("Last digit of {} is 0 and is 0".format(number))
    else:
        print("Last digit of {} is -{} and is less than 6 and not 0".format(number, last_digit))

else:
    print("Last digit of {} is 0 and is 0".format(number))

