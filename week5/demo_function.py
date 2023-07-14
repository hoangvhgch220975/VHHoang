# def hi(name):                   #name is a parameter
#     print ('Hi' ,name)

# hi('Peter')                     # John is an argument
# hi('John')
# name = input('Enter name ')
# hi(name)                           #name is an argument


# def hello_world():
#     print('Hello Python world')
# hello_world()
# hello_world()




def find_max(a, b):
    if a > b:
        return a
    else:
        return b
    print('This line will never be executed')

m= find_max(10,20)
print(m)    

#write a function calculatr  the average of 3 grades and return it

def average(a,b,c):
    total = a + b + c
    ave = total / 3
    return ave
math = 9
english = 9.5
physical = 7
ave=average(math,english,physical)
print('Average ', ave)