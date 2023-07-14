# # Do following excersice

# # Ex1

def print_line(n):
    for i in range(n+1):
        for j in range(i):
            print('*',' ', end='')
        print()
n = int(input("Enter the number:   "))
print_line(n)


Ex2
def print_reversed(n):
    for i in range(n+1):
        for j in range(i):
            print('*',' ', end='')
        print()
n = int(input("Enter the number:   "))
print_reversed(n)
## have somthing wrong ................


def print_triangle(n):
    for i in range(n+1,1,-1):
        for j in range(i-1):
            print('*',' ', end='')
        print()
n = int(input("Enter the number:   "))
print_triangle(n)



#Ex3
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
present = True
while present :
    num = int(input("Input number: "))
    if num <= 1:
        print('Invalid number')
    elif prime(num) :
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")
    ask = input('Continue? [y/n]   ')
    present = ask == 'y'


#Ex4
def print_prime(n):
    # Helper function to check if a number is prime
    def check_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Iterate from 2 to n (inclusive) and print the prime numbers
    for num in range(2, n + 1):
        if check_prime(num):
            print(num)

n = int(input("Please enter a number: "))
print_prime(n)
        
#Ex5
# I don't know how to do ................