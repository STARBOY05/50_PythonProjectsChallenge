# Making a List of Alphabets to search for the index
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher():
    result = True
    while(result):
        choice = input("What you want to do? e - encode d - decode or exit: ")
        text = input(("Enter your message: ")).lower() # Convert the message into lowercase if in uppercase
        shift_number = int(input("Enter the shifting number: "))
        if shift_number >= 26: # if shift number exceeds num of alphabets
            shift_number = shift_number % 25 # Using the remainder as the shift number
        CC_text = ""
        # Start the looping across the letters of the text
        for letter in text:
            if letter in alphabet:
                index = alphabet.index(letter) # First find the index of each letter
                if(choice == 'e'):
                    index = index + shift_number # increment the index with the shifting number
                elif(choice == 'd'):
                    index = index - shift_number # decrement the index with the shifting number  
                CC_text += alphabet[index] # store it in declared variable
            # For spaces, number, symbols 
            else:
                CC_text += letter
        print(f"The text is {CC_text}")
        choice = input("Would you like to continue? --  yes, no: ")
        if(choice == "no"):
            result = False # break the loop

caesar_cipher()
