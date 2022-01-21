print("Welcome to the Secret Auction!")

auction_list = {} # creating the bidders list oops i meant dictionary
result = True # condition for loop

def highest_bidder(biddings):
    highest_bid = 0
    winner = ""
    for person in biddings: # looping through keys
        bid_amount = biddings[person] # storing the value of each key
        if(bid_amount > highest_bid): # comparing for the highest bid
            highest_bid = bid_amount
            winner = person
    print(f"\nThe winner is {winner} with a bid of whopping ${highest_bid}")

while(result):
    name = input("What is your name?: ") 
    bid = int(input("What's your bid?: $"))
    auction_list[name] = bid # adding the person as key and bid as value in dictionary
    ask = input("Are there any other bidders? Type 'yes' or 'no': ")
    if(ask == "no"):
        result = False
        highest_bidder(auction_list)