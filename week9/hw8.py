def book_management(books):
    total = 0
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        if choice == 1:
            add_book(books)
        elif choice == 2:
            edit_book_price(books)
        elif choice == 3:
            search_book(books)
        elif choice == 4:
            total += sell_book()
        elif choice == 5:
            show_total(total)
        elif choice == 6:
            print_all_books(books)
        elif choice == 0:
            print('Close program-----------')
            running = False
        else:
            print('Invalid choice, try again')
def print_menu():
    print('0. Close program')
    print('1. Add new books')
    print('2. Edit books price')
    print('3. Search for books')
    print('4. Sell books')
    print('5. Show total')
    print('6. Print all books')

def add_book(books):
    new_book = input('Enter new book: ')
    price = float(input('Enter a price: '))
    if new_book not in books:
        books[new_book] = price
        print(f'The book {new_book} already added successfully')
    else:
        print(f' The book {new_book} has already been added')

def edit_book_price(books):
    edit_book = input('Enter a book you want to edit: ')
    new_price = float(input('Enter a new price: '))
    if edit_book in books:
        books[edit_book] = new_price
        print(f'The book {edit_book} has been edit successfully')
    else:   
        print(f' The book {edit_book} has not already existed')

def search_book(books):
    search_book = input('Enter the book you want to search : ')
    if search_book in books: 
        print(f' The book {search_book} has found' )
        print(f'{search_book} : {books[search_book]}')
    else: 
        print(f'The book {search_book} has not existed')

def sell_book():
    sell_book = input('Enter the book you want to sell: ')
    if sell_book in books: 
        total = books[sell_book]
        del books[sell_book]
        print(f'The book {sell_book} has sold successfully ')
        return total
    else: 
        print(f'The book {sell_book} has not existed')
        return 0

def show_total(total):
    print(f'Total Sales: $:  {total}')
    

def print_all_books(books):
    print('Book catalog: ',books)


books = {}
book_management(books)




        
        

