#format number
a = 3.1415926
s = '3.14'
print(f'{a:8.2f}', '***')  #number is rignt aligned
print(f'{s:8}', '***')      # string is left aligned

print(f'|{a:>8.2f}|') #right aligned
print(f'|{a:<8.2f}|') #left aligned
print(f'|{a:^8.2f}|') #center aligned

print(f'{a:8.2f}') 
print(f'{a:8.2e}')
print(f'{a:8.2%}')



s = 'Hello python world'
print(s.lower()) #change all characters to lower case
print(s.upper()) #change all characters to upper case
print(s.title()) #change first character of each word to upper case
print(s.swapcase()) #change upper case to lower case and vice versa




name1 = 'Lohn Lemon' 
name2 = 'Paul McCartney'
print(len(name1)) #length of string
print(name1[0]) #First character of string
if name1 > name2: 
    print(name1, 'is greater than', name2)
else:
    print(name1, 'is less than or equal to', name2)
print(max(name1 ,name2)) #compare twq strings, return the greater one
print(min(name1, name2)) #compare twq strings, return the smaller one

#sring operations
a = 'Helle'
b = 'World'
s = a + ' '+ b
print(s)    
print(a*4)


#Slicing (similar to list slicing)
a = 'Hello world'
print(a[:5]) # from beginning to position 4
print(a[-5]) # from -5 to end

#check if a string contains a substring
print(s)
if 'hello' in s.lower():
    print('Found hello')

#String classification: if a string contains only letters, digits, etc
print('Hello'.isalpha()) #True
print('Hello123'.isalpha()) #False
print('123'.isdigit()) #True
print('123.45'.isdigit()) #False
print('123.45'.isdecimal()) #False
print('123'.isdecimal()) #True
print('123'.isnumeric()) #true
print('123.45'.isnumeric()) #False

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



s = '         hello World        '
s = s.strip() #remove leading and trailing spaces
s = s.title() #chang first character of each word to upper case
print(s)

s = s.strip().title() 


s = 'Hello python world'
s_list = s.split() #split string in to list of words
print(s_list)

language = 'python,jave,c,c++,cpp,javescript'
lang_list = language.split(',') #split string in to list of words
print(lang_list)
print(f'There are {len(lang_list)} languages')