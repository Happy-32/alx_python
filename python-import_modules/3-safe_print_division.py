#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        dividend = a / b
    except Exception as e:
        return None
    finally:
        print("Inside Result: {}".format(dividend))
        return dividend

# print(safe_print_division(10,5))
# print(safe_print_division(12,2))
# print(safe_print_division(10,2))