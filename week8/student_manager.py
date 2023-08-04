def student_management():
    names = []
    gpas = []
    
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        if choice == 1:
            add_student(names, gpas)
        elif choice == 2:
            delete_student(names, gpas)
        elif choice == 3:
            edit_student(names, gpas)
        elif choice == 4:
            search_student(names, gpas)
        elif choice == 5:
            print_student(names, gpas)
        elif choice == 6:
            print('Program closed successfully')
            running = False
        else:
            print('Invalid choice, please try again')
def print_menu():
    print('1.Add student')
    print('2.Delete student')
    print('3.Edit student')
    print('4.Search students')
    print('5.Display student')
    print('6.Quit program')

def add_student(names, gpas):
    name = input('Enter student name: ')
    gpa = float(input('Enter student GPAs: '))
    names.append(name)
    gpas.append(gpa)
    print(f'student {name} added successfully')

def delete_student(names,gpas):
    name = input('Enter student name: ')
    for i in range(len(names)):
        if names[i] == name:
            name.pos(i)
            gpas.pos(i)
            print(f'student {name} deleted successfully')
            return
    print(f'student {name} not found')
def edit_student(names,gpas):
    name = input('Enter student name: ')
    new_gpa = float(input('Enter new gpa: '))
    for i in range(len(names)):
        if names[i] == name:
            gpas[i] = new_gpa
            print(f'student {name} edited successfully')
            print(f'student {name} new gpa: {new_gpa}')
            return
        print('student {name} not found')
def search_student(names, gpas):
    search_gpa = float(input('Enter the GPA: '))
    same_gpa = []
    for i in range(len(gpas)):
        if gpas[i] >= search_gpa:
            same_gpa.append(gpas[i])
    print(f'There are {len(same_gpa)} students have GPA >= {search_gpa}')
    

def print_student(names, gpas):
    for i in range(len(names)):
        print(f'{names[i]} : GPA = {gpas[i]}')

student_management()