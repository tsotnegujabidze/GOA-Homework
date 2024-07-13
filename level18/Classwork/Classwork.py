#დავალება N1

list = []

for i in range(10):
    list.append(i)

print(len(list)) 

#დავალება N2

list = []

input1 = int(input("What is the first number?> "))
input2 = int(input("What is the second number?> "))

for i in range(input1 + 1, input2):
    list.append(i) 

print(list)

#დავალება N3

list = []

starting_number = int(input("What is the starting number?> "))
last_number = int(input("What is the last number?> "))

for i in range(starting_number + 1, last_number):
    list.append(i)

print(min(list))
print(max(list))
print(sum(list))

#დავალება N4

list = []

quantity_of_numbers = int(input("How many numbers would you like to input?> "))

for i in range(quantity_of_numbers):
    lister = int(input("Start entering the numbers> "))
    list.append(lister)

print(sum(list))

#დავალება N5
list = ["Porsche", "Lamborghini", "BMW", "Mercedes", "Audi"]

first_three = list[0:3]
last_two = list[3:6]

print(first_three)
print(last_two) 

print(list[-3])
print(list[-4]) 


#დავალება N6
list = ["Tsotne", "Luka", "Nika", "Andria", "Tsotne", "Nia"]

for names in list:
    if names == "Tsotne":
        print("Hello admin!")
    else:
        print("Hello user!")