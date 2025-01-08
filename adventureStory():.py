def intro():
    print("""
    You find yourself at a corn maze on halloween night playing around with your friend. 
    They dare you to go and the maze and have a race to see who makes it out first, without 
    knowing the maze it really haunted.
    """)
    
    choice = input("Do you wanna go 'left' or 'right'? ").lower()
    
    if choice == 'left':
        killer_clown()
    elif choice == 'right':
        zombies()
    else: 
        print("Invalid choice. Try again. ")
        intro()
        
def killer_clown():
    print("""
    If you choose left, you will come across a killer clown you can choose to run away or fight
    him with your weapon Stand your ground, use your only weapon and fight the clown, risking everything for a 
    chance to defeat him and escape the maze. Then you take his weapon to add to your inventory
    Turn and run, hoping to lose the clown in the twisting paths.
    """)
    
    choice = input("Do you want to 'run' away or 'fight?' ")
    
    if choice == 'run':
        scarecrow()
    elif choice == 'fight':
        die("The clown will stab you and you die.")
    else: 
        print("Invalid choice. Try again. ")
        killer_clown()
        
def zombies():
    print("""
    If you choose right you will come across a zombie, you can choose to fight the zombie 
    or run away Stand your ground, use your only weapon and fight the zombie, risking everything for 
    a chance to defeat him and escape
    """)
    
    choice = input("Do you want to 'run' or 'fight'? ")
    
    if choice == 'run':
        die("The scarecrow army trapped you and ate your brain. ")
    elif choice == 'fight':
        win("run away and escape. ")
    else: 
        print("Invalid choice. Try again. ")
        zombies()
        
def scarecrow():
    print("""
    If you defeat the challenges you go deeper into the maze then come across a battle army of 
    scarecrows and they surround you. left
          """)
    
    choice = input("Do you want to go 'left' or 'right'? ")
    
    if choice == 'left':
        die("You get stuck at the dead end and the scarecrows attack you. ")
    elif choice == 'right':
        win()
    else: 
        print("  ")
        scarecrow()
        
def win():
    print("\nYou find the exit")
    print("You have espaced the haunted maze ")
    print("Good job, you made it out alive!")
    play_again()
    
def die(reason):
    print("\nGAME OVER : " + reason)
    play_again()
    
def play_again():
    choice = input ("\nDo you want to play again? (yes/no): ").lower()
    if choice == 'yes':
        intro()
    else: 
        print("Thanks for playing!")
        
#Start the game
intro()    
                   
