import random

while True:
    # showing choices to user
    print("****** Enter your choice*******")
    print('''
    r for rock
    p for paper
    s for scissor
    ''')
    # enter your choice
    your_choice=input('Your choice: ')
    if your_choice=='r' or your_choice=='p' or your_choice=='s':
        pass
    else:
        print("Invalid choice !! Choose again \n\n")
        continue

    # generate random number and assign certain alphabet accordingly
    computer_choice=random.randint(1,3)
    if computer_choice==1:
        computer_choice='r'
    elif computer_choice==2:
        computer_choice='p'
    else:
        computer_choice='s'

    print(f"Computer: {computer_choice}")
    # taking decision to declare winner or loser
    if your_choice=='r' and computer_choice=='s':
        print("You Win")
    elif your_choice=='p' and computer_choice=='r':
        print("You Win")
    elif your_choice=='s' and computer_choice=='p':
        print("You Win")
    elif your_choice==computer_choice:
        print("Wow same choice!")
    else:
        print("You Lose")
    print("\n\n")
