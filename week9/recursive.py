def rec_sum(n):
    if n == 1:
        return 1
    else:
        return rec_sum(n-1) + n
print(rec_sum(10))

def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1) * n
print(factorial(10))

def fibonacci(n):
    if n <= 0:
        raise ValueError ('n must be positive')
    if n ==1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

try :
    n = int(input('Enter a number: '))
    print(f'Fibonacci number {n} is {fibonacci(n)}')
except ValueError:
    print('Invalid input')