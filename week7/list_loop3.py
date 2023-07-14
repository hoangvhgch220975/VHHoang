import random as rd
numbers = rd.sample(range(1,100),10)         # create a list of 10 random numbers from 1 to 99
print(numbers)

count = 0
for n in numbers:
    if n % 2 == 0:
        count += 1
print(f'The number of even numbers: {count}')

