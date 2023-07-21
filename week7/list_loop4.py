products = ['notebook', 'pencil', 'pen', 'eraser', 'ruler','shapener']
stocks = [100, 120, 80, 50, 60, 90]
prices = [2.5, 1.5, 2.0, 1.0, 1.5, 1.0]
# #Count how many products that hve total values greater than 100
# count = 0
# for i in range(len(stocks)):
#     value = stocks[i] * prices[i]
#     if value > 100:
#         count += 1
# print(f'The item have values greater than 100 is: {count}')

#Enter the product name, print the price and stock
name  = input('Enter the product name: ')
found_pos = None
for i in range(len(products)):
    if products[i] == name:
        found_pos = i
        break
if found_pos == None:
    print(f'Product {name} it not found')
else:   
    print(f'Price: {prices[found_pos]}, Stock: {stocks[found_pos]} ')

#Find products with price >= 2.0
found_products = []
for i in range(len(prices)):
    if prices[i] >= 2.0:
        found_products.append(products[i])
if len(found_products) == 0:
    print( "No products found")
else:
    print('Found products ',end='')
    print()

#Find products with total values <= 150
count = 0
for i in range(len(prices)):
    if stocks[i] * prices[i] > 150:
        count += 1
if count == 0:
    print('No products have total values >= 150 ')
else :
    print('Found products have total values >= 150 ')