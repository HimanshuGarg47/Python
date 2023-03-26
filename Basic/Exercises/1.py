samplestr = "Twinkle, twinkle, little star,\n\t\t How I wonder what you are! \n\t\t\t\tUp above the world so high,\n\t\t\t\t Like a diamond in the sky. \nTwinkle, twinkle, little star,\n\t\t How I wonder what you are"

# print(samplestr)
import sys
from platform import python_version
# print(sys.version)
# print(python_version())

from datetime import time, date, datetime

# print(datetime(2023, 12,12, 8, 8, 8))
# print(date.today())
# print(time())

from math import pi
# rad = int(input("Enter radius of circle\n"))
# area_cir = rad**rad *pi
# print(area_cir)


# fname, lname = input("Enter first and last name").split()
# print(f"{lname} {fname}")


# seq = input("Enter seq of numbers with comman space\n")
# arr = seq.split(', ')
# tuparr = tuple(arr)
# print(arr)
# print(tuparr[0])
import os
# filename = input("Enter filename\n")
# print(os.path.basename(filename))
import random
import string
print("Generate a random color hex:")
print("#{:6x}".format(random.randint(0, 0xFFFFFF)))
print("\nGenerate a random alphabetical string:")
# print(string.ascii_letters + "\n\n")
max_length = 255
s = ""
for i in range(random.randint(1, max_length)):
    s += random.choice(string.ascii_letters)
print(s)

print("Generate a random value between two integers, inclusive:")
print(random.randint(0, 10))
print(random.randint(-7, 7))
print(random.randint(1, 1))
# print("Generate a random multiple of 7 between 0 and 70:")
# print(random.randint(0, 10) * 7)
print("\n\n")
arr = [1, 2, 3, 4, 5,6]
print(random.choice(arr))