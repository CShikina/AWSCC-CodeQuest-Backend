ans_yes=["Yes", "yes"]
ans_no=["No", "no"]
    
print("Hello, AWS! Come play a little adventure game with me :D")

print("\nYou are at home and you hear a knock on your door and see a man asking for shelter.")

ans_1=input("\nWill you let him enter your home? (Yes/No): ")

if ans_1 in ans_yes:
    ans_2=input("\nPolice arrived and asked whether thief is inside. Will you say Yes or No?")
    if ans_2 in ans_yes:
        print("\nCongratulations, you win!")
    elif ans_2 in ans_no:
        print("\nYou lose, game over.")
    else:
        print("\nInvalid answer")

elif ans_1 in ans_no:
    ans_3=input("\nHe attacked you. Will you knock him down?")
    if ans_3 in ans_yes:
        print("\nCongatulations, you win!")
    elif ans_3 in ans_no:
        print("\nYou lose, game over.") 
    else:
        print("Invalid answer") 
        
else:
    print("Invalid answer.")    

    