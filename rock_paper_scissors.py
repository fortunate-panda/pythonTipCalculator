import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
shapes = [rock, paper, scissors]



computer_choice = random.choice(shapes)



choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")





if choice == "0":

  print(shapes[0])

  print("Computer chooses:\n")

  print(computer_choice)

  if computer_choice == shapes[0]:

    print("It's a tie")

  elif computer_choice == shapes[1]:

    print("You lose...")

  elif computer_choice == shapes[2]:

    print("You win!")



elif choice == "1":

  print(shapes[1])

  print("Computer chooses:\n")

  print(computer_choice)

  if computer_choice == shapes[0]:

    print("You win!")

  elif computer_choice == shapes[1]:

    print("It's a tie.")

  elif computer_choice == shapes[2]:

    print("You lose...")



elif choice == "2":

  print(shapes[2])

  print("Computer chooses:\n")

  print(computer_choice)

  if computer_choice == shapes[0]:

    print("You lose...")

  elif computer_choice == shapes[1]:

    print("You win!")

  elif computer_choice == shapes[2]:

    print("It's a tie.")



else:

  print("That is not an option.")