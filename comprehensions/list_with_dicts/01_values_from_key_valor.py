def extract_values(items):
    return [item["valor"] for item in items]

data = [
    {"nome": "A", "valor": 10},
    {"nome": "B", "valor": 0},
    {"nome": "C", "valor": 25},
]
print(extract_values(data))
