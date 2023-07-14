from random import randint
playing = True
while playing:
    user_choice = input('Choose: rock, paper or sissors: ')
    if user_choice not in ['rock', 'paper', 'sissors']:
        print('Error')
    else:
        computer_choice = randint(1,3)
        if computer_choice == 1:
            computer_choice = 'rock'
        elif computer_choice == 2:
            computer_choice = 'paper'
        else:
            computer_choice = 'sissors'
        if computer_choice == user_choice: print('Draw')
        elif computer_choice == 'rock' and user_choice == 'paper': print('You win')
        elif computer_choice == 'rock' and user_choice == 'sissors': print('You lose')
        elif computer_choice == 'paper' and user_choice == 'rock': print('You lose')
        elif computer_choice == 'paper' and user_choice == 'sissors': print('You win')
        elif computer_choice == 'sissors' and user_choice == 'rock': print('You win')
        else: print('You lose')
    ask = input('Do you want to play again? (y/n): ')
    playing = ask == 'y' 
