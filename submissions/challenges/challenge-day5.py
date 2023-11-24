# random.randint() to randomly assign between a-b
# random.choice() to randomly assign between stated elements
# random.shuffle() to shuffle elements

import random
game = ["rock", "paper", "scissors"]
rock = "rock"
paper = "paper"
scissor = ["scissors", "scissor"]

print("ROCK, PAPER, SCISSOR GAME\n")

print("Enter your choice. (Rock, paper, scissor)\n")
player = input(">>").lower()
computer = random.choice(game)

if player in rock:
    if computer in rock:
        print(f"\nIt's a tie! Computer chose {computer}")
    elif computer in paper:
        print(f"\nYou lose. Computer chose {computer}")
    elif computer in scissor:
        print(f"\nYou win! Computer chose {computer}")
    else:
        print("Invalid input")
        
elif player in paper:
    if computer in rock:
        print(f"\nYou win! Computer chose {computer}")
    elif computer in paper:
        print(f"\nIt's a tie! Computer chose {computer}")
    elif computer in scissor:
        print(f"\nYou lose. Computer chose {computer}")
    else:
        print("\nInvalid input")
        
elif player in scissor:
    if computer in rock:
        print(f"\nYou lose. Computer chose {computer}")
    elif computer in paper:
        print(f"\nYou win! Computer chose {computer}")
    elif computer in scissor:
        print(f"\nIt's a tie! Computer chose {computer}")    
    else:
        print("\nInvalid input")

else:
    print("Invalid input")

