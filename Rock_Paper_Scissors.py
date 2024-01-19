import random

rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''
paper = '''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''
scissors = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
game = ([rock, paper, scissors])
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper and 2 for scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("choose a number from 0-2\n You Lose")
else:
    print(game[user_choice])
    if user_choice >= 3 or user_choice < 0:
        print("choose a number from 0-2\n You Lose")
    computer_choice = (random.randint(0,2))
    com = game[computer_choice]
    if user_choice > computer_choice:
        print(f"computer choose {com}\n YOU WIN")
    elif user_choice ==0 and computer_choice == 2:
        print(f" computer choose {com}\n YOU WIN")
    elif user_choice == computer_choice:
        print(f'computer choose {com}\n It\'s a draw')
    else:
        print(f"computer choose {com}\n YOU LOSE")
