def filter_odd(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers 


def even_sum(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return sum(even_numbers) 


def odd_index_sum(numbers):
    total_sum = 0
    for i in range(1, len(numbers), 2):
        total_sum += numbers[i]
    return total_sum