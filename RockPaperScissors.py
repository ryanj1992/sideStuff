import random
game = ['Rock', 'Paper', 'Scissors']

while True:
    player = input("Rock, Paper or Scissors?")
    computer = random.choice(game)
    if player == computer:
        print(computer)
        print("Draw! Try Again")
    elif player == 'Rock':
        if computer == 'Scissors':
            print(computer)
            print("You Win!")
        else:
            print(computer)
            print("You loose!")
    elif player == 'Paper':
        if computer == 'Scissors':
            print(computer)
            print("You Loose!")
        else:
            print(computer)
            print("You Win!")
    elif player == 'Scissors':
        if computer == 'Rock':
            print(computer)
            print("You Loose!")
        else:
            print(computer)
            print("You Win!")
    else:
        finished = input("Do you wish to exit?")
        if finished == 'y':
            False
        else:
            True
     