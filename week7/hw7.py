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
    print('book not found')

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
      
      
