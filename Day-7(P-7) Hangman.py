import random
# Python will choose from the below list
word_list = ["ant","baboon","badger","bat","bear","camel","cat","cobra",
    "crow","deer","dog","donkey","duck","eagle","fox","frog","goat","goose","hawk",
    "lion","lizard","llama","mole","monkey","mouse","owl","panda",
    "parrot","pigeon","python","rabbit","ram","rat","rhino" "salmon","seal","shark","sheep",
    "sloth","snake","spider","swan","tiger","toad","turkey","turtle",
    "weasel","whale","wolf","zebra"]
chosen_word = random.choice(word_list)
# To get the length of the word
word_len = len(chosen_word)

# Blanks for guessing the word
display = []
for i in range(word_len):
    display += "_"
print(display)
# condition to terminate while loop
end_of_game = False

while not end_of_game:
    guess_letter = input("Guess a letter: ").lower()
    for index in range(word_len):
        letter = chosen_word[index]
        if(letter == guess_letter.lower()):
            display[index] = letter
    print(display)
    if "_" not in display:
        end_of_game = True
        print(f"Congratulations! Solution is {chosen_word}")