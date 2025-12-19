def maior_ou_menor(values):
    return ["maior" if v > 10 else "menor" for v in values]

numbers = [5, 12, 3, 20, 8]
print(maior_ou_menor(numbers))
