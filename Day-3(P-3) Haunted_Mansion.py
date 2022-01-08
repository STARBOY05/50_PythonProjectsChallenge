print("Welcome to Haunted Mansion.")
print("Your Mission is to find the treasure box.")
print("Choose your decisions wisely\n")

print("Your are at the START point(Main Door)\n")
choice = input("Press U to go Upstairs, D to go Downstairs: ")
if(choice == "U"):
    print("Great Choice! You are in a room on the top floor")
    print("You try to search the whole room for the treasure but there is darkness all over")
    choice = input("You found a switch and it can help in searching more quickly... Press Y to switch on the light , N for No: ")
    if(choice == "Y"):
        print("Oops!! That was a bad idea as the ghost can see you and tear you to pieces for his delicious dinner")
        print("You Lose. GAME OVER!!!")
    elif(choice == "N"):
        print("You thought that if light was on it would also help the ghost to find you easily..")
        print("You see out from the window where two trees have colored dots on it")
        print("You jump out of the window... BAMM!! You fall but you are okay!!")
        print("Two colors Red and Blue and a board which said...") 
        print("THE GAME IS NOW GOING TO END!!! Choose wisely...")
        choice = input("Which color do you choose? R or B")
        if(choice == "R"):
            print("OH! you chose the color of blood now you might see one coming out of your body")
            print("You Lose. GAME OVER!!!")
        elif(choice == "B"):
            print("CONGRATULATIONS!! You won the treasure...")
        else:
            print("INVALID CHOICE!!!")
    else:
        print("INVALID CHOICE!!!")
elif(choice == "D"):
    print("You entered the basement where spider webs and coffins are laid all over.")
    print("You guess that the mansion might have been locked for more than 25 years.")
    print("You think that the treasure could have been hidden in the coffins as the size of coffins are huge")
    choice = input("You encountered a large coffin. Press O to open it , N to to check something else")
    if(choice == "O"):
        print("Oh No!! The deads are buried in here how can you think that a treasure must have been hidden here.")
        print("Oh You see a hand of one of the dead moving..You freak out!!! The same hand catches you and pulls you inside the coffin...")
        print("You Lose. GAME OVER!!!")
    elif(choice == "N"):
        print("Gosh!! You guessed that coffins must not be touched as it will make squeak noises and alert the ghosts...")
        print("You search further and find a door which might open to the the backyard of the house")
        print("You opened it and yes there were two trees having colored dots...RED and BLUE and a board which said...")
        print("THE GAME IS NOW GOING TO END!!! Choose wisely...")
        choice = input("Which color do you choose? R or B")
        if(choice == "R"):
            print("OH! you choosed the color of blood now you might see one coming out of your body")
            print("You Lose. GAME OVER!!!")
        elif(choice == "B"):
            print("CONGRATULATIONS!! You won the treasure...")
        else:
            print("INVALID CHOICE!!!")
    else:
        print("INVALID CHOICE!!!")
else:
    print("INVALID CHOICE!!!")