def only_positive(values):
    return [v for v in values if v > 0]

nums = [-3, 0, 2, 10, -1, 5]
print(only_positive(nums))
