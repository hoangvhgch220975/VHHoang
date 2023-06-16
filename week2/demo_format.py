name =input('Enter you name: ')
age =int(input('Enter your age: '))
gpa =float(input('Enter your gpa: '))

print(f"{'Name':<20}{'Age':>3}{'GPA':>5}")
print(f"{name:<20}{age:>3}{gpa:>5}")

massage = 'Hello'
print(f'|{massage:>20}|')
print(f'|{massage:<20}|')
print(f'|{massage:^20}|')
print(f'|{massage:20}|')

n=100
print(f'|{n:>20}|')
print(f'|{n:<20}|')
print(f'|{n:^20}|')
print(f'|{n:20}|')

PI= 3.141592651564
print(f'|{PI:>20.2f}|')
print(f'|{PI:<20.4f}|')
print(f'|{PI:^20.6f}|')
print(f'|{PI:20.8f}|')
