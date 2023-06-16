# # # # 3.
number1_str = input(" First number: ")
number2_str = input("Second number: ")
number1 = int(number1_str)
number2 = int(number2_str)
combination = number1 *  number2
print(f"Answer: {combination}")

print()
input("Press return to continue ...")


# # # # 4.

number1 = int(input('First number: '))
number2 = int(input('Second number: '))
combination = number1 / number2
print(f"Answer: {combination}")

print()
input("Press return to continue ...")


# # # 5.
from random import randint


min = int(input('Min(>4): '))
max = int(input('Max: '))
random1 = randint(min, max)
random2 = randint(min, max)
random3 = randint(min, max)
random4 = randint(min, max)
random5 = randint(min, max)

print(f"{random1} {random2} {random3} {random4} {random5}")

print()
input("Press return to continue ...")


# # 6. 
import random as rd

name = str(input('Input your name: '))
x = rd.randint(1,100)
print('Hello ', name, ', your lucky number is ', x)


# 7.

import random as rd
name = str(input('Enter your name: '))
year = int(input('Enter your birth year: '))

x = rd.randint(year,year+70)
print('Hello ', name, ', your lucky year is ', x)


