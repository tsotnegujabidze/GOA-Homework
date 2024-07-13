#პროგრამა N1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        print(num)

#პროგრამა N2
names = ["Luka", "Nika", "Anano", "Lile", "Irakli", "Leo"]

for name in names:
    if name.startswith('L'):
        print(name)


#პროგრამა N3
numbers = [1, 6, 3, 8, 5, 10, 4, 7]

count = 0

for num in numbers:
    if num > 5:
        count += 1

print(f"There are {count} numbers greater than 5.")
