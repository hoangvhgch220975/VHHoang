import random as rd
numbers = rd.sample(range(1,100),10)         # create a list of 10 random numbers from 1 to 99
print(numbers)

# sum of numbers
s = 0
for n in numbers:
    s = s + n       # s+=n
print(f'SUm of numbers: {s}')

s = 0
for i in range(len(numbers)):
    s = s + numbers[i]
print(f'SUm of numbers: {s}')
# find the maximum number in list
max = numbers[0]
for n in numbers:
    if n > max: 
        max = n
print(f'Max of numbers: {max}')

for i in range(len(numbers)):
    if numbers[i] > max:
        max = numbers[i]
print(f'Max of numbers: {max}')

# find the minimum number in list
min = numbers[0]
for n in numbers:
    if n < min:
        min = n
print(f'Min of numbers: {min}')

for i in range(len(numbers) ):
    if numbers[i] < min:
        min = numbers[i]
print(f'Min of numbers: {min}')
