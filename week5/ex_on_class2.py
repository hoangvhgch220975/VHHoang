#write a function to calculate the interest of a bank account
#parameters:
# - Balance: the current balance of the account
# - month: the number of the month
# if month < 6, the interest rate is 0.5%
# if month >=6, the interest rate is 0.8%
# return the mew balance (old balance + interest )



balance = float(input('Enter the balance: '))                                                 
month = int(input('Enter the month: '))
def interest_rate(balance):
    if month < 6:
        new_balance = balance * (5 /100) * month
    if month >=6:
        new_balance = balance * (8 /100) * month
    new_balance = new_balance + balance
    return new_balance
print("New Balance: ", interest_rate(balance))





balance = float(input('Enter the balance: '))
month = int(input('Enter the month: '))

def interest_rate(balance):
    new_balance = balance * rate * month
    new_balance = new_balance + balance
    return new_balance
if month < 6: 
    rate = 5 / 100
else: rate = 8 / 100
print("New Balance: ", interest_rate(balance))