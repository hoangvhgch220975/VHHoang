for i in range(10):
    print(i,'hello ')

for i in range(0,10,2):
    print(i,'hello')

for i in range(10,0,-1):
    print(i,'hello')

#Sum from 1 to 10:
n = int(input('Enter n:   '))
s = 0
for i in range(1,n+1):
    s += i
print('Sum from 1 to ',n,'is: ',s)
