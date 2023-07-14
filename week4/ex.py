# # Calculate n!

# n = int(input('Enter the number: '))
# factorial = 1
# for i  in range(1,n+1):
#     factorial *=i
# print('n! =',factorial)



# # Calculate sum of even numbers from 1 to n:

# n = int(input('Enter the number: '))
# s = 0
# for i in range(1,n+1):
#     if i%2 == 0:
#         s += i
# print('s =',s)


# # Calculate product of odd numbers from 1 to n:


# n = int(input('Enter the number: '))
# product = 1
# for i in range(1,n+1):
#     if i%2 != 0:
#         product *= i
# print('product =',product)



# # Print the mutiplication table of n:
# n = int(input('Enter the number: '))
# mul = 1
# for i in range(1,11):
#     mul = n*i
#     print(f'{n:2} x {i:2} = {mul:5}')

# # Mested for loop
# # Print triangle of asterisks
# n = int(input('Enter the number: '))
# for i in range(n+1):
#     for j in range(i):
#         print('*', end='' )
#     print()
 

#5.1: Print triangle of numbers
# 1
# 2 2
# 3 3 3 
# 4 4 4`4`

# n=int(input('Enter the number'))
# for i in range(n+1):
#     for j in range(i):
#         print(i,' ', end='' )
#     print()

#5.2 Print triangle of numbers
#1
#1 2
#1 2 3
#1 2 3 4
n=int(input('Enter the number'))
for i in range(n+1):
    for j in range(i):
        print(j+1,' ', end='' )
    print()