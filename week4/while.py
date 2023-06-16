#while scenario 1: asking user to continue
stop = False
while not stop: 
    product = input('Enter product: ')
    sold = int(input('Enter sold: '))
    price = float(input('Enter price: '))
    print('Product: ', product, 'Sold: ', sold, 'Price: ', price)
    anwser =input('Continue? (y/n): ')
    stop = anwser == 'n'

    print('Product: ', product)