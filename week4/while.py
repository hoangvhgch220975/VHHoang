#while scenario 1: asking user to continue
# stop = False
# while not stop: 
#     product = input('Enter product: ')
#     sold = int(input('Enter sold: '))
#     price = float(input('Enter price: '))
#     print('Product: ', product, 'Sold: ', sold, 'Price: ', price)
#     anwser =input('Continue? (y/n): ')
#     stop = anwser == 'n'

#while scenario 2: validating values
valid_input = False
while valid_input == False:
    name =  input('Enter name: ')
    age = int(input('Enter age: '))
    if age < 0 or age > 120:
        print('Invalid age')
    valid_input = age >= 0
print('Name: ', name, 'Age: ', age)