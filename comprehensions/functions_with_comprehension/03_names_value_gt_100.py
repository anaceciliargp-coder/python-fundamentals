def names_over_100(items):
    return [item["nome"] for item in items if item["valor"] > 100]

data = [
    {"nome": "Mouse", "valor": 80},
    {"nome": "Teclado", "valor": 150},
    {"nome": "Monitor", "valor": 900},
    {"nome": "Cabo", "valor": 20},
]
print(names_over_100(data))
