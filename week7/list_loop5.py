book = ['John', 'Peter', 'Mary', 'Jane', 'Tom', 'Jenny', 'Alice', 'Bob']
department = ['IT', 'GD', 'IT', 'Biz', 'Biz','GD', 'IT', 'GD']
GPAs = [3.5, 3.0, 3.2, 3.6, 3.8, 3.9, 3.7, 3.4]   


# #1.Enter book name, find book and print him/her GPA and department
check = False
bookName = input('Enter book name: ')
for i in range(len(book)):
    if book[i] == bookName:
        check = True
        print('Found book')
        print('His/her GPA is: ', GPAs[i])
        print('He/ she is in: ', department[i])
if check == False:  
        print('book not found ')

# #2.Enter dependent name, find book in that department and print their name and GPA
departmentName = input('Enter department name: ')
departmentbook = []
pos_department = 0
GPA = []
for i in range(len(department)):
    if departmentName == department[i]:
        pos_department = i
        departmentbook.append(book[pos_department])
        GPA.append(GPAs[pos_department])
print(departmentbook)
print()
print(GPA)

#3.Enter best book(Highest GPA)
bestbook = GPAs[0]
for i in range(len(GPAs)):
    if GPAs[i] > bestbook:
        bestbook = GPAs[i]
print(f'The best book is {book[i]} with GPA {bestbook}')
#4.Enter a GPA, count how many books hace GPA >= that GPA
GPA = input('Enter a GPA: ')
count = 0
for i in range(len(GPAs)):
    if GPAs[i] >= float(GPA):
        count += 1
print('These are', count, ' book have GPA >= ', GPA)

#Calculate average GPA of books in all departments
All_average = 0
sum = 0
for i in range(len(department)):
    sum += GPAs[i]
    All_average = sum / (len(department))
print (' The average of all books in all departments is ','%.2f'% All_average)

# Calculate average GPA of books in each departments

IT_average = []
GD_average = []
Biz_average = []
result =0
ave = 0
for i in range(len(department)):
    if department[i] == 'IT':
        IT_average.append(GPAs[i])
    if department[i] == 'GD':
        GD_average.append(GPAs[i])
    if department[i] == 'Biz':
        Biz_average.append(GPAs[i])
for i in range(len(IT_average)):
    result += IT_average[i]
ave = result / (len(IT_average))
print (' The average of all books in IT is: ','%.2f'%ave)
ave = 0
result = 0

for i in range(len(GD_average)):
    result += GD_average[i]
ave = result / (len(GD_average))
print (' The average of all books in IT is: ','%.2f'%ave)
ave = 0
result = 0

for i in range(len(Biz_average)):
    result += Biz_average[i]
ave = result / (len(Biz_average))
print (' The average of all books in IT is: ','%.2f'%ave)
      
      
