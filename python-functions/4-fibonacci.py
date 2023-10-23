#!/usr/bin/env python3
def fibonacci_sequence(n):
    fib_seq = [0, 1]
    if n <= 0:
        fib_seq = []
    elif n == 1:
        fib_seq = [0]
    else:
        for i in range(2, n):#n not inclusive
            next_digit = fib_seq[i-1] + fib_seq[i-2]
            fib_seq.append(next_digit)
    return fib_seq