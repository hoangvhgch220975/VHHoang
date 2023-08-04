#print contents
f = open('languages.txt', 'r') #open file with read mode
contents = f.read() # read all contents into a string
languages = contents.split("\n")
print(len(languages))
for lan in languages:
    print(lan)
f.close() # close file


f = open('languages.txt', 'r')
lines = f.readlines() # read all contents into a list of strings
f.close() 

for language in lines:
    print(f'|{language.strip()}|') #strip () removes the newline characters

# Use this method for large file
f = open('languages.txt', 'r')
line = f.readline() 

while line != '':
    print(line.strip())
    line = f.readline() #read the next line

f.close()

#Exercise: read agencles.txt file, find agencies that has 'Authority'  in their name. and print them out
invalid_files = True
while invalid_files:
    try:
        file_name = input('Enter file name: ')
        f = open(file_name, 'r')
        invalid_files = False
    except FileNotFoundError:
        print(f'File {file_name} not found. Try again.')
        
lines = f.readlines()

for i, line in enumerate(lines):
    if 'Authority' in line:
        print(i+1, line.strip())
