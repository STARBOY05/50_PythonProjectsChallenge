import random
letterslist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbolslist = ['+','-','*','/','(',')','[',']','@','!','#','$','%']
numberslist = ['0','1','2','3','4','5','6','7','8','9']

print("Welcome to the Password Generator!\n")
letters = int(input("How many letters would you like to have in your password? "))
syms = int(input("How many symbols would you like? "))
nums = int(input("How many numbers would you like? "))

# Weak Password
# password = ""
# for char in range(1,letters+1):
#     password += random.choice(letterslist)
# for sym in range(1,syms+1):
#     password += random.choice(symbolslist)
# for num in range(1,nums+1):
#     password += random.choice(numberslist)
# print(password)

# ****Note**** As letters,symbols and numbers are in sequence, hackers can easily guess some parts of the password 

# Strong Password
generate_password_list = []
generate_password = ""
for char in range(1,letters+1):
    generate_password_list.append(random.choice(letterslist))
for sym in range(1,syms+1):
    generate_password_list.append(random.choice(symbolslist))
for num in range(1,nums+1):
    generate_password_list.append(random.choice(numberslist))
random.shuffle(generate_password_list)
for i in generate_password_list:
    generate_password += i
print(f"Your Password is {generate_password}")