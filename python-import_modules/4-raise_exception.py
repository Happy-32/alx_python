#!/usr/bin/python3
def raise_exception():
    raise ValueError("404 Error")

try:
    print("Try Block")
    raise_exception()  # Call the function to raise the exception
except TypeError as te:
    print("Error Occurred:", te)
