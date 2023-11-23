print("Enter your choice: Rock, Paper, Scissors.")

rock=["Rock", "rock"]
paper=["Paper", "paper"]
scissors=["Scissors", "scissors"]

player1=input("Player 1: ")
player2=input("Player 2: ")
    
if player1 in rock:
    if player2 in paper:
        print("Player 2 wins!")
        
    elif player2 in scissors:
        print("Player 1 wins!")
        
    elif player1 and player2 in rock:
        print("It's a tie")
        
    else:
        print("Invalid input")
        
elif player1 in paper:
    if player2 in rock:
        print("Player 1 wins!")
        
    elif player2 in scissors:
        print("Player 2 wins!")
        
    elif player1 and player2 in paper:
        print("It's a tie.")
        
    else:
        print("Invalid input.")

elif player1 in scissors:
    if player2 in paper:
        print("Player 1 wins!")
        
    elif player2 in rock:
        print("Player 2 wins!")
        
    elif player1 and player2 in scissors:
        print("It's a tie!")
        
    else:
        print("Invalid input.")
        
else:
    print("Invalid input.")
        