def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result

print(safe_print_division(10, 2))
print(safe_print_division(10, -2))
print(safe_print_division(0, 2))
print(safe_print_division(10, 0))
print(safe_print_division(0, 0))