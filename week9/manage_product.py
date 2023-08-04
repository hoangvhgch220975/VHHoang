def manage_product(products):
    running = True
    while running:
        print_menu()    
        choice = int(input("Select your choice: "))
        if choice == 1:
            add_product(products)
        elif choice == 2:
            delete_product(products)
        elif choice == 3:
            edit_product(products)
        elif choice == 4:
            filter_product(products)
        elif choice == 5:
            display_product(products)
        elif choice == 0:
            print('Close program')
            running = False
        else:
            print('Invalid choice, try again')
def print_menu():
    print('O Close program')
    print('1.Add Product')
    print('2.Delete Product')
    print('3.Edit Product')
    print('4.Filer Product')
    print('5.Display Product')

def add_product(products):
        name = input('Enter Product Name: ')
        if name in products:
            print(f'Product {name} already exists')
            return
        price = float(input('Enter Price: '))
        products[name] = price
        print(f'Product {name} added successfully')
        

def delete_product(products):
    name = input('Enter Product Name: ')
    if name in products:
        del products[name]
        print('Delete Product successfully')
    else:
            print(f'Product {name} not exists. Please, try again')

def edit_product(products):
    name = input('Enter Product Name: ')
    new_price = input('New Price: ')
    if name in products:
        products[name] = new_price
        print('Edit product successfully')
    else:
        print(f'Product {name} not exists. Please, try again')

def filter_product(products):
    filter_price = float(input('Enter Price: '))
    for name in products:
        price = products[name]
        if price >= filter_price:
            print('Found product: ')
            print(f'{name} {price}')
    # for name, price in products.items():
    #     if price >= filter_price:
    #         print('Found product: ')
    #         print(f'{name} {price}')

def display_product(products):
    print('Products: ',products)

products = {}
manage_product(products)





