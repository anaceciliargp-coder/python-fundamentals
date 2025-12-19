def names_gt_50(items):
    return [item["nome"] for item in items if item["valor"] > 50]

data = [
    {"nome": "Caderno", "valor": 30},
    {"nome": "Mochila", "valor": 120},
    {"nome": "Fone", "valor": 200},
]
print(names_gt_50(data))
