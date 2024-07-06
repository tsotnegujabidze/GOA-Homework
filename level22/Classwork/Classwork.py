#დავალება N1
def calculate_average():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(sum(numbers) / len(numbers))

calculate_average() 

#დავალება N2
def greet_user(user_name = "Guest"):
    print(f"Welcome {user_name}!")

greet_user("luka")

#დავალება N3
def manual_sum(list):
    total = 0
    for num in list:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
print("Sum of numbers:", manual_sum(numbers))

#დავალება N4
def print_even_numbers(n):
    for i in range(2, n + 1):
        if i % 2 == 0:
            print(i)

print_even_numbers(10)

#დავალება N5
def organize_list(numbers_list):
    for i in numbers_list:
        if i % 2 == 0:
            print(f"Even: {i}")
        else:
            print(f"Odd: {i}")

organize_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) 

#დავალება N6
def sum(num1, num2):
    print(num1 + num2)

sum(int(input("What is the first number?> ")), int(input("What is the second number?> ")))

#დავალება N7
def concetenate_strings(str1, str2):
    return(str1 + str2)

print(concetenate_strings(input("What is the first number?> "), input("What is the second number?> ")))

#დავალება N8
def find_maximum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

print(find_maximum(int(input("What is the first number?> ")), int(input("What is the second number?> "))))

#დავალება N9
def reverse_string(the_word):
    return the_word[::-1]

print(reverse_string(input("What it the word which you want to reverse?> ")))

#დავალება N10
def calculate_area(height, width):
    area = height * width
    return area

print(calculate_area(int(input("What is the height of the rectangle?> ")), int(input("What is the width of the rectangle?> "))))

# დავალება N11
def count_vowel(The_word):
    vowels = ["a", "e", "i", "o", "u"]
    list_of_vowels = []
    for i in The_word:
        if i in vowels:
            list_of_vowels.append(i)
    print("Vowels in the word:", list_of_vowels)

count_vowel(input("What is the word?> "))

# დავალება N12
def make_capital(word):
    print(word)

make_capital(input("Enter the word> ").capitalize())
