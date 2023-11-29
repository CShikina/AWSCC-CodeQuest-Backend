#Shopping list 
shoppingList = []
numChoice = 0

while (numChoice != 4):
    print("Options: \n1. Add item to the shopping list\n2. View shopping list\n3. Remove item from the shopping list\n4. Quit")
    numChoice = input("Enter the number of your choice: ")
    
    if numChoice == "1":
        sl1 = input("Enter the item you want to add: ")
        shoppingList.insert(0, sl1)
        print(f"{shoppingList[0]} has been added to your shopping list.\n")
        
    elif numChoice == "2":
        print(f"{shoppingList}\n")
        
    elif numChoice == "3":
        remove = input("Enter the item you want to remove: ")
        shoppingList.remove(remove)
        print(f"{remove} has been removed from your shopping list.\n")
        
    else:
        print("Goodbye!")
        break
   
        
        
    
        
    