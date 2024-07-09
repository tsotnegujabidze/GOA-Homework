def capitalize(name):
    return name.capitalize()
print(capitalize(input("Enter your name> ")))

def upper(name):
    return name.upper()
print(upper(input("Enter your name> ")))


# # # #Difference between method and function is that function can be used for every data type while
# # # #method is only used for one exact type

# # # #capitalize method makes first letter of the word capital while upper method makes all the letters capital


word = input("Enter word with uppercase> ")

print(word.lower())

word = "Tsotne Gujabidze"

print(word.count("a"))


# # #string is any text between either '' or "".

# # #lower method returns strings in lowercase.

# # #count methods counts letters or words in a sentece given by us.



sentence = "GOA is the best"

x = sentence.find("t")

print(x)

sentence = "GOA is the best"

x = sentence.index("G")

print(x)


# # #just like find function, index function also searchs for a specified letter or word which  we input
# # #in the sentence (which we also input). The difference is that if we there is no such a letter or word 
# # #in the sentence which we gave, then index method returns error, while find method return -1.

email_list = []

quantity = int(input("How many times do you want to enter differnet gmail?> "))

for i in range(quantity):
    email = input("Enter email address> ")
    email_list.append(email)

for email in email_list:
    if email.endswith('@gmail.com'):
        print("Thanks!")
    else:
        print("Invalid gmail. gmail has to end with @gmail.com")

# #startwith method checks if following sentence starts with word or letter specified by us

# #endwith method checks if following sentence ends with word or letter specified by us


