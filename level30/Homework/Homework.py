def odd_index_sum(numbers):
    total_sum = 0
    for i in range(1, len(numbers), 2):
        total_sum += numbers[i]
    return total_sum

