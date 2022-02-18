# ----------------------------------------------------The Coffee Machine -- Digital Version----------------------------------------
# Requirements
# Menu, Price, Resources
MENU = {
    "Espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "Latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "Cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
COIN_VALUES = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01,
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

# To check whether sufficient resources are available for order
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Machine >>> Sorry, there is not enough {item}")
            return False
    return True

# To check whether the required money is transferred by the customer
def is_transaction_successful(money_recieved,drink_cost):
    change = 0
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost,2)
        print(f"Machine >>> Here is your ${change} returned.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Machine >>> Sorry that's not enough money. Money refunded...")
        return False

# Transaction Amount
def process_coins():
    total = 0
    print("Machine >>> Please insert coins: ")
    for coin,value in COIN_VALUES.items():
        total += int(input(f"Enter the number of {coin}s: ")) * value
    return total

# Deduction of the resources
def make_coffee(drink,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Cashier >>> Here is your order -- {drink} ☕. Thank You and Drink again!")

# -------------------------------Working of Coffee Machine----------------------------------------
is_on = True

# Take the order
while is_on:
    choice = input("Cashier >>> What would you like: (Espresso, Latte, Cappuccino): ")
    if choice == "OFF":
        is_on = False
    elif choice == "Report" or choice == "report":
        print(f"Water = {resources['water']}ml")
        print(f"Milk = {resources['milk']}ml")
        print(f"Coffee = {resources['coffee']}g")
        print(f"Money = ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            amount = process_coins()
            if is_transaction_successful(amount,drink['cost']):
                make_coffee(choice,drink['ingredients'])
                print("\nCashier >>> Next Customer Please..")
        else:
            print("Cashier >>> Sorry Sir! Come back tomorrow.")
# ----------------------------------------------- END ----------------------------------------------
