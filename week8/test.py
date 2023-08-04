#String classification: if a string contains only letters, digits, etc
print('Hello'.isalpha()) #True
print('Hello123'.isalpha()) #False
print('123'.isdigit()) #True
print('123.45'.isdigit()) #False
print('123.45'.isdecimal()) #False
print('123'.isdecimal()) #True
print('123'.isnumeric()) #true
print('123.45'.isnumeric()) #False

#
#Search method: find, startwith, endwith, count
s = 'Hello world'
msg = input('Enter a sub string: ')
i=s.find(msg)
if i == -1:
    print(msg,'not found')
else:   
    print(msg,'found')
if s.startswith('Hell'):
    print(f'{s} starts with Hell')
if s.endswith('World'):
    print(f'{s} ends with World')

print(f'{s} contains {s.count("l")} l')
print(f'{s} contains {s.count("o")} o')