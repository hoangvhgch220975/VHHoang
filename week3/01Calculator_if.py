number1 = int(input('First number: '))
number2 = int(input('Second number: '))
operation = input('Operation [+, -, *, /, //, %, **]: ')
if operation == '+':
    combination = number1 + number2
elif operation == '-':
    combination = number1 - number2
elif operation == '*':
    combination = number1 * number2
elif operation == '/':
    combination = number1 / number2
elif operation == '//':
    combination = number1 // number2
elif operation == '%':
    combination = number1 % number2
else:
    combination = number1 ** number2
print(f'Answer:{combination}')



# if operation not in ['+','-','*','/','//','%','**']: 
    # print('Invalid value')