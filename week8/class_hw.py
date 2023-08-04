# Exercises: 
#enter product: sneaker
#enter price: 20
# prints out: your invoice
# product     | sneaker
# price       | 20
#VAT          |2.00
# #Total        |22.00



# product = input('Enter product: ')
# price = float(input('Enter price: '))
# VAT = (price / 100)*10
# total = price + VAT
# print(f"{'Product':10}|{product:>10}")
# print(f"{'Price':10}|{price:10}")
# print(f"{'VAT':10}|{VAT:10.2f}")
# print(f"{'Total':10}|{total:10.2f}")




#Exercises: Ask user to enter a list of fruits, separated by commas
#Print how many fruits are there
#Ask for a favorite fruit, print if it is in the list or not
#Example output
#enter fruits: apple, banana, orange,grapes
#thera are 4 fruits
#Enter favorite fruit: apple
#apple is in the list



fruits = input('Enter fruit: ')
fruit_list = fruits.split(',')
print(f'There are {len(fruit_list)} fruit')
fav_fruit = input('Enter favorite fruit: ')
if fav_fruit in fruit_list:
    print(f'{fav_fruit} is in the list')
else :
    print(f'{fav_fruit} is not in the list')

i = fruits.find(fav_fruit)
if i == -1:
    print(f'{fav_fruit} is not the list')
else :
    print(f'{fav_fruit} is in the list')