groceries = [ 'apple', 'orange', 'lemon', 'kiwi','coconuts']
prices = [2.5, 4.5 ,4.0, 5.5, 3.5]
# Fing the fruit that has the highest price
i_max = 0
price_max = prices[0]
for i in range(len(prices)):
    if prices[i] > price_max:
        price_max = prices[i]
        i_max = i
print(f'The highest price fruit is { groceries[i_max]} with price { price_max}')

i_min = 0
price_min = prices[0]
for i in range(len(prices)):
    if prices[i] < price_min:
        price_max = prices[i]
        i_min = i
print(f'The lowest price fruit is {groceries[i_min]} with price {price_min}')