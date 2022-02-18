
# Creating the necessary funcs for calculation
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b

# Asking for user input
calc = True
while(calc):
    First_num = float(input("Enter the first number: "))
    Second_num = float(input("Enter the second number: "))
    oper = input("Pick an operation you want to apply to these to numbers + - * / : ")
#  Do the operations accordingly
    if(oper == '+'):
        result = add(First_num,Second_num)
        print(f"{First_num} {oper} {Second_num} = {result}")
    elif(oper == '-'):
        result = sub(First_num,Second_num)
        print(f"{First_num} {oper} {Second_num} = {result}")
    elif(oper == '*'):
        result = mul(First_num,Second_num)
        print(f"{First_num} {oper} {Second_num} = {result}")
    elif(oper == '/'):
        result = div(First_num,Second_num)
        print(f"{First_num} {oper} {Second_num} = {result}")
    else:
        print("Invalid Operation")
    choice = input("Do you want to calculate again? 'Y' or 'N': ")
    if choice == 'N':
        calc = False