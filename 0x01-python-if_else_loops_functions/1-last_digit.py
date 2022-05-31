#!/usr/bin/python3
from contextlib import nullcontext
import random
# number = random.randint(-10000, 10000)
number = "hello"
try:
    last_digit = int(repr(number)[-1])
except ValueError:
    raise TypeError("Only integers are allowed")
if number < 0:
    last_digit *= -1
str_val = None
if last_digit > 5:
    str_val = "and is greater than 5"
elif last_digit == 0:
    str_val = "and is 0"
else:
    str_val = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} {str_val}")
