# THE BLACK JACK GAME

import random 
# Introduction to the game
print("Welcome to the game of BLACK JACK")

# 2 - 10 normal 10 - J,K,Q , 1 or 11 - A
cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
def Deal_Card():
    card = random.choice(cards)
    return card

# To calculate score from the in-hand cards 
def calculate_score(cards):
    # BlackJack condition
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # A in card and total is > 11 then A can change from 11 to 1
    if 11 in cards and sum(cards) >= 11:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# To compare the user's score with the computer and give a decision.
def compare(user_score,comp_score):
    if user_score == comp_score:
        return "Draw !"
    if comp_score == 0:
        return "You Lose the game!"
    elif user_score == 0:
        return "Win with a BLACKJACK!"
    elif user_score > 21:
        return "Above 21, You Lose!"
    elif comp_score > 21:
        return "Opponent went above 21, You win!"
    elif user_score > comp_score:
        return "You Win!"
    else:
        return "You Lose"

# MAIN FUNCTION
def play_game():
    # Initialize both the list of card holdings to 0
    user_cards = []
    comp_cards = []
    # Looping condition
    is_game_over = False
    # Each player will get two cards
    for _ in range(2):
        user_cards.append(Deal_Card()) 
        comp_cards.append(Deal_Card())
    # loop until game is not over
    while not is_game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
        print(f"Your Cards: {user_cards} , Current Score: {user_score}")
        print(f"Computer's First Card: {comp_cards[0]}")
        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if(user_deal == 'y'):
                user_cards.append(Deal_Card())
            else:
                is_game_over = True
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(Deal_Card())
        comp_score = calculate_score(comp_cards)
    
    # To get the winner of BLACKJACK 
    print(f"Your final cards: {user_cards} , Final Score: {user_score}")
    print(f"Computer's final cards: {comp_cards} , Final Score: {comp_score}")
    print(compare(user_score,comp_score))

while input("Do you want to play? Type 'y' for yes 'n' for no: ") == 'y':
    play_game()

