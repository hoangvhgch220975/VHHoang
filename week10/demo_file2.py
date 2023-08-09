# invalid_files = True
# while invalid_files:
#     try:
#         file_name = input('Enter file name: ')
#         f = open(file_name, 'r')
#         invalid_files = False
#     except FileNotFoundError:
#         print(f'File {file_name} not found. Try again.')
        
# lines = f.readlines()
# f.close()
 
# #reopen another file to save authotities
# f = open(file_name + '.authotity', 'w')
# for i, line in enumerate(lines):
#     if 'Authority' in line:
#         print(i+1, line.strip())
#         f.write(line)
# f.close()

#exercises: read authors.txt, find all authors that we gmail and save them into a new file gmail_authors.txt in following format:
# Paul Bakaus: paul.bakaus@gmail.com
# Richard Worth: rdworth@gmail.com

try: 
    f= open('authors.txt','r')
    lines = f.readlines()
    f.close()
except FileNotFoundError:
    print('File not found')

if lines:
    with open('gmail_authors.txt', 'w') as f:
        for line in lines:
            if 'gmail' in line:
                author = line.split('<')[0] .strip()
                email = line.split('<')[1].strip().strip('>')
                f.write(f'{author} : {email} \n')

