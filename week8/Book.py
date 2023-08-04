def book_management():
    titles = []
    author = []
    genre = []
    public_year = []
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        if choice == 1:
            add_book(titles, author, genre, public_year)
        elif choice == 2:
            delete_book(titles, author, genre, public_year)
        elif choice == 3:
            edit_book(titles, author, genre,public_year)
        elif choice == 4:
            search_book(titles, author, genre, public_year)
        elif choice == 5:
            print_book(titles, author, genre, public_year)
        elif choice == 6:
            print('Program closed successfully')
            running = False
        else:
            print('Invalid choice, please try again')
def print_menu():
    print('1.Add book')
    print('2.Delete book')
    print('3.Edit book')
    print('4.Search books')
    print('5.Display book')
    print('6.Quit program')

def add_book(titles, author, genre, puclic_year):
    book_name = input('Enter book name: ')
    writer = input('Enter the author name: ')
    book_type = input('Enter the book genre: ') 
    year = input('Enter the public year: ')
    titles.append(book_name)
    author.append(writer)
    genre.append(book_type)
    puclic_year.append(year)
    print(f'book {book_name} added successfully')

def delete_book(titles, author, genre,puclic_year):
    book_name = input('Enter book name: ')
    for i in range(len(titles)):
        if titles[i] == book_name:
            titles.pos(i)
            author.pos(i)
            genre.pos(i)
            puclic_year.pos(i)
            print(f'book {book_name} deleted successfully')
            return
    print(f'book {book_name} not found')
def edit_book(titles, author, genre, public_year):
    book_name = input('Enter book name: ')
    new_writer =input('Enter new author: ')
    new_type = input('Enter new genre: ')
    new_year = input('Enter new public year: ')
    for i in range(len(titles)):
        if titles[i] == book_name:
            author[i] = new_writer
            genre[i] = new_type
            public_year[i] = new_year
            print(f'book {book_name} edited successfully')
            print(f'book {book_name} new author: {new_writer}, new genre: {new_type}, new public year: {new_year}')
            return
        print(f'The book {book_name} not found')
def search_book(titles, author, genre, public_year):
    






    
    print(f'There are {len(same_gpa)} books have GPA >= {search_gpa}')
    

def print_book(names, gpas):
    for i in range(len(names)):
        print(f'{names[i]} : GPA = {gpas[i]}')

book_management()