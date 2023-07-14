#shopping list

item_list = []
print('Welcome to my store!')
check = True
while check:
    item = (input('Enter the item you want to buy(Press Enter to finish): '))
    if item == '':
        check = False
        break
    item_list.append(item)
offer =str(input('Which item?(all/index): '))
if offer == 'all':

    print('Your shopping list is: ', item_list)
elif offer == 'index':
    choose = int(input('Enter the number of the item you want: '))
    print('Your shopping list is: ', item_list[choose-1])
else:
    print('Invalid option')



#guest list 
guest_list = []
print('Welcome to the party!')
count = int(input('How many guest here? '))
for i in range(1, count+1):
    guest_list.append(input(f"Enter the name of guest {i}: "))
offer = (input('Do you want remove any guest?(Yes/No) '))
if offer == 'yes':
    guest_remove = str(input('Enter the name of guest you want to remove: '))
    if guest_remove not in guest_list: 
        print('No one will be able to remove')
    else:
        guest_list.remove(guest_remove)
        print('Your guest list is: ',guest_list)
elif offer == 'no':   
    print('Your guest list is: ', guest_list)