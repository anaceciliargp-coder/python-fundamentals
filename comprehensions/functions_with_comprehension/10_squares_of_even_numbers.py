def squares_of_evens(values):
    return [v ** 2 for v in values if v % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(squares_of_evens(numbers))
