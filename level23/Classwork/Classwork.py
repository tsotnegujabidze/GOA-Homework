# # #დავალება N1
def add(num1, num2):
    sum = num1 + num2
    return sum
print(add(int(input("Enter first number> ")), int(input("Enter second number> "))))


# #დავალება N2
def calculate(num1, num2, sign):
    if sign == "+":
        return num1 + num2
    elif sign == "-":
        return num1 - num2
    elif sign == "x":
        return num1 * num2
    elif sign == ":":
        return num1 / num2
    else:
        print("Invalid sign.")
print(calculate(int(input("Enter the first number> ")), int(input("Enter the second number> ")), input("Enter the sign> ")))

#დავალება N3
def strings(string1, string2):
    result_list = []
    result_list.append(string1)
    result_list.append(string2)
    return result_list

print(input("What is the first string?> "), input("What is the second string?> "))