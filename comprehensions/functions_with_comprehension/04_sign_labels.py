def sign_labels(values):
    return ["positivo" if v > 0 else ("zero" if v == 0 else "negativo") for v in values]

numbers = [-3, 0, 5, -1, 10]
print(sign_labels(numbers))
