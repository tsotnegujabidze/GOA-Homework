# #დავალება N1
# def plus_five(number):
#     new_number = number + 5
#     return new_number
# print(plus_five(int(input("What is the number?> "))))

#დავალება N2
# def multiply(num1, num2):
#     miltiplied_num = num1 * num2
#     return miltiplied_num
# print(multiply(int(input("What is the first number?> ")), int(input("What is the second number?> "))))

#დავალება N3
# def string_lenght(word):
#     word_lenght = len(word)
#     return word_lenght
# print(string_lenght(input("What is the word?> ")))

# დავალება N4
# def list_lenght(list):
#     lenght_of_list = len(list)
#     return lenght_of_list
# print(list_lenght(["Luka", "Nika", "Andria", "Tsotne", "Salome"]))

# დავალება N5
# def is_palindrome(word):
#     if word == word[::-1]:
#         print("Yes")
#     else:
#         print("No")

# is_palindrome(input("What is the word?> "))

# დავალება N6
def longest_string(word1, word2):
    words = [word1, word2]
    if len(words[0]) > len(words[1]):
        print(words[0])
    else:
        print(words[1])

longest_string(input("What is the first word?> "), input("What is the second word?> "))

# დავალება N7
