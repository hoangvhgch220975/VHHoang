
#shoping list
guest_list = []
guest_num  = int(input("How many guests will be attending the party? "))

for i in range(1, guest_num + 1): guest_list.append(input(f"Enter the name of guest {i}:"))
print(f"The final guest list is: {guest_list}")
remove_question = input("Do you want to remove any guests from the list? (yes/no): ")
guest_remove = input("Enter the name of the guest to remove: "); print("wtf guest ?") if guest_remove not in guest_list else guest_list.remove(guest_remove);print(f"Guest {guest_remove} has been removed from the list.");print(f"The updated guest list is: {guest_list}") if remove_question.lower == "yes" else print(f"Last guest list: {guest_list}")




# #Guest list
# list = []; wtf_conditional = "WTF input"; accept = True
# print("Welcome to the Grocery Store! \nEnter the items you want to buy (press Enter to finish):")
# while accept: 
#     insert_item = input(f"Item {len(list) + 1}:")
#     if insert_item != "": list.append(insert_item) 
#     else: accept = False
# for count, i in enumerate(list, start = 1): print(f"{count}: {i}")
# choose_item = input("Which item? (all/index): ")
# if choose_item.replace(" ", "").isalpha() or choose_item.replace(" ", "").isdigit():
#     if choose_item.replace(" ", "").isalpha(): print(wtf_conditional) if choose_item.lower() != "all" else print(f"Your Shopping List: {list}")
#     else: print(wtf_conditional) if int(choose_item) > len(list) else print(f"Your item: {list[int(choose_item) - 1]}")
# else: print(wtf_conditional)