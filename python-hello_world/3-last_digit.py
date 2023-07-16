#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = str(number)[-1]
def is_greater(last_digit):
    if int(last_digit) > 5:
        return "and is greater than 5"
    elif int(last_digit) == 0:
        return "and is zero"
    elif int(last_digit) < 6 and int(last_digit) != 0:
        return "and is less than 6 and not 0"

res = is_greater(last_digit)
if number > 0:
    print("Last digit of {} is {} {}".format(number,last_digit, res))
elif number < 0:
    print("Last digit of {} is -{} {}".format(number,last_digit, res))