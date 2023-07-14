# write a fucntion print_slogan
# parameters:
# -Slogan: a string 
# - symbol: a string

def write_slogan(slogan, symbol):
    length = len(slogan)
    line = symbol*(length+2)
    print(line)
    print(f'{symbol}{slogan}{symbol}')
    print(line)
slogan = input("Enter slogan ")
symbol = input('Enter symbol ')
write_slogan(slogan, symbol)
