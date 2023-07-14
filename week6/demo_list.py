#Declare the list
a = [] # empty list
b = ['1', '2', '3'] # list of 3 elements of string
c = [1,2,3] # list of 3 elements of integers
d = [1.5, 0.4, -2.3] # list of 3 elements of floats
e = [True, False, False] # list of 3 elements of booleans
f = [1, '2', 3.0, True] # list of 4 elements of different types

# List operators: +, *, in, not in
g = b + c               #concatneate 2 lists
print(g)
h = c * 2                  # duplicate a list
print(h)
if 2 in c:
    print('2 is in c')
if 100 not in c:
    print('100 is not in c')

import random as rd
# function for list: len(), min(), max(), sum()
numbers = rd.sample(range(1,100),10) # generate 10 random numbers from 1 to 99
print(numbers)
print(len(numbers))  # length of a list
print(min(numbers))  # minimum value of a list
print(max(numbers))  # maximum value of a list
print(sum(numbers))  # sum of all value of a list
sorted_number = sorted(numbers)  # return a new list of sorted values, original list is not changed
print(sorted_number)
sorted_number = sorted(numbers, reverse=True) # return a new list of sorted values in reverse order
print(sorted_number)



# list functions: append(), insert(), remove(), pop(), clear()
a = [1,2,3]
a.append(4)  # append 4 to the end of the list
print(a) 
b = ['a', 'b', 'c']
a.append(b) # append a list to the end of the list
print(a)
print(len(a))

a.insert(1,1000) # insert 100 at index 1
print(a)
a.pop() # remove the last element
print(a)
a.remove(100) # remove the first element with value 100
print(a)



a = [1,2,3,2,4,2]
a.remove(2) #remove the 1st element with value 2
print(a)
a.clear() #remove all elements
print(a)


# Accessing list elements: zero-based indexing
a=rd.sample(range(1,100),10)
print(a)
print(a[0]) #first element
print(a[9]) #last element

#Negative index: from -1 to -n
print(a[-1])
print(a[-10])

#Slicing a list (simple form): list[start:end]
b = a[1:4]  # get the new list from index 1 to 3
print(b)
c = a[5:9]  # get the new list from index 5 to 8
print(c)
d = a[:4]  # get the first 4 elements
print(d)
e = a[6:]  # get the last 4 elements
e = a[-4:]
print(e)
f = a[1:6:2]  #start from 1 to 6, skip 2 elements
g = a[: : 2]  #start from 0 to end, skip 2 elements


#using sliceing to reverse a list 
print(a[::-1]), # start from end, skip 1 element, up to beginning.