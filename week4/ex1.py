#ex4

# n = int(input("What size square? "))                  
# for i in range(n):                                
#     draw = ''
#     for j in range(n):
#         draw +='*=' 
#     print(draw)


#ex5

# row = int(input("How many rows do you want? "))
# col = int(input("How many columns do you want? "))
# for i in range(row):
#     for j in range(col):
#         print('*', end = '')
#     for k in range(col):
#         print('=', end = '')
#     print()
        


#ex6
from random import randint

min = int(input("Min = "))
max = int(input("Max = "))
n_rand = int(input("How many random numbers do you want? "))
out = ''
for i in range(n_rand):
    out = randint(min, max)
    if out ==0 :
        print("Bad luck, no random values for you")
        exit()
    elif out == 7:
        continue
    print(f' {out}', end ='')  
