def format_items(items):
    return [f"Produto: {item['nome']} | Valor: R${item['valor']:.2f}" for item in items]

data = [
    {"nome": "Mouse", "valor": 80},
    {"nome": "Teclado", "valor": 150},
    {"nome": "Cabo", "valor": 20},
]
print(format_items(data))
