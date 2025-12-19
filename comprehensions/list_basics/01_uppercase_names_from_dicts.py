data = [
    {"nome": "caneta", "valor": 5},
    {"nome": "livro", "valor": 40},
    {"nome": "mochila", "valor": 120},
]
upper_names = [item["nome"].upper() for item in data]
print(upper_names)
