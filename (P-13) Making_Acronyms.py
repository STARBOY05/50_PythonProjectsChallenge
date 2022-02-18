# Creation of Acronyms

# User Input
user_input = str(input("Enter a Phrase: "))

# Split all the given text in a list
text = user_input.split()

a = "" # empty string
# Remove the first letter from each element
for i in text:
    a = a + str(i[0]).upper()
print(a)