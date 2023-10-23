#!/usr/bin/env python3

def validate_password(password):
    if len(password) < 8:
        return False
    upper = False
    lower = False
    digit = False
    for character in password:
        if character.isupper():
            upper = True
        elif character.islower():
            lower = True
        elif character.isdigit():
            digit = True
        
    if not (upper and lower and digit):
        return False
    
    if ' ' in password:
        return False
    return True