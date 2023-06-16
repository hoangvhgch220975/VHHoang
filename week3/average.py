math = float(input('Enter your math point: '))
liter =float(input('Enter your liter point: '))
eng = float(input('Enter your eng point: '))

if ( 0 <= math <= 10) and ( 0 <= liter <= 10) and ( 0 <= eng <= 10): 
    average = ((math + liter + eng))/3
else:
    print('invalid value')
    exit()
if average > 10 :
    print("invalid value")
elif average < 4.0 :
    print('fail')
elif (4.0 < average < 6.5) :
    print('pass')
elif (6.5 < average < 8.0) :
    print('Merit')
else:  print('Distinction')

