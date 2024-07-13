#დავალება N1
def use_number(num1, num2):
    return num1 + num2, num1 - num2, num1 * num2, num1 / num2
print(use_number(int(input("Enter the first number> ")), int(input("Enter the second number> "))))

#დავალება N2
def add_until_100(a, b):
    while a < 100:
        a += b
    return a
print(add_until_100(int(input("Enter the first number> ")), int(input("Enter the second number> "))))

#დავალება N3
def is_it_even(number):
    if number % 2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")
is_it_even(int(input("Enter the number> ")))

# დავალება N4
def max_num(list):
    return max(list)
print(max_num([1, 2, 3, 6, 12, 51, 44, 11]))
