#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Check if the key exists in the dictionary
    if key in a_dictionary:
        # If the key exists, replace the value
        a_dictionary[key] = value
    else:
        # If the key doesn't exist, add a new key/value pair
        a_dictionary[key] = value

    return a_dictionary
