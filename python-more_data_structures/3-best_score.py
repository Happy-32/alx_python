#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    # Check if the dictionary is empty
    if len(a_dictionary) == 0:
        return None

    # Initialize the maximum value and corresponding key
    max_value = float('-inf')
    max_key = None

    # Iterate over each key-value pair in the dictionary
    for key, value in a_dictionary.items():
        # Check if the value is greater than the current maximum value
        if value > max_value:
            max_value = value
            max_key = key

    return max_key
