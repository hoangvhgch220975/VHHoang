try:
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = a/b
    print(f'{a} / {b} = {c}')
except ValueError as e:
    print('Error',e)
except ZeroDivisionError as e: 
    print('Error',e)


def get_int(prompt):
    while True:
        try :
            a = int(input(prompt))
            return a
        except ValueError:
            print('Invalid input, try again')
a = get_int('Enter a number: ')
b = get_int('Enter b number: ')

print(f'{a} + {b} = {a+b}')
            