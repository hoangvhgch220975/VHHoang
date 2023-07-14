import random
playing = True
dict = ['rock', 'sissors', 'paper']
while playing:
    user_choose = input("choose rock, sissors, paper: ")
    if user_choose not in dict: print("invalid input")
    else: 
        computer = random.choice(dict)
        if computer == user_choose: print("tie!")
        elif computer == 'rock' and user_choose == "paper": print("you win")
        elif computer == 'sissors' and user_choose == "rock": print("you win")
        elif computer == 'paper' and user_choose == "sissors": print("you win")
        else: print("you lose")
        option = input('do you want to play: ')
        if option == 'n': playing = False
        else: playing = True