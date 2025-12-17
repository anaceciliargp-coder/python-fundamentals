def list_values(items):
    values = []
    for item in items:
        values.append(item["valor"])
    return values


if __name__ == "__main__":
    data = [{"nome": "Livro", "valor": 40}, {"nome": "Caneta", "valor": 5}, {"nome": "Mochila", "valor": 120}]
    print(list_values(data))
