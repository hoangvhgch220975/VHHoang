name = str(input('Enter name of product: '))
price = float(input('Enter price: '))
stock = int(input('Enter stock:'))
value = price * stock

print('+', '-'*20, '+', '-'*10, '+', '-'*5, '+', '-'*10, '+')
print(f"|{'Name':<20} {'|':>3} {'Price':>10} {'|':>3} {'Stock':>7} {'|':>1} {'Value':>10} {'|':>3}")
print('+', '-'*20, '+', '-'*10, '+', '-'*5, '+', '-'*10, '+')



print(f"|{name:<20} {'|':>3} {price:>10.2f} {'|':>3} {stock:>7} {'|':>1} {value:>10} {'|':>3}")
print('+', '-'*20, '+', '-'*10, '+', '-'*5, '+', '-'*10, '+')

