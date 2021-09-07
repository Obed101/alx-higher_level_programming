#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

def last_digit(n):
    """Returns the last digit of n."""
    n = str(n)
    return int(n[len(n)-1])
if last_digit(number) > 5:
    print("Last digit of {} is {} and is greater\
 than 5".format(number, last_digit(number)))
elif last_digit(number) == 0:
        print("Last digit of {} is {} and is \
zero".format(number, last_digit(number)))
elif last_digit(number) < 6 and last_digit(number) != 0:
        print("Last digit of {} is {} and is less\
 than 6 and not 0".format(number, last_digit(number)))
