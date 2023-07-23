import random

number = random.randint(-10000, 10000)

def last_num(number):
    return abs(number) % 10
print(number)
last = last_num(number)
print(last)
# if number > 0:
#     print(number, "is greater than zero")
#     last_digit = last_num(number)
#     if last_digit > 5:
#         print("Last digit of {} is {} and is greater than 5".format(number, last_digit))
#     elif last_digit == 0:
#         print("Last digit of {} is 0".format(number))
#     else:
#         print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_digit))
