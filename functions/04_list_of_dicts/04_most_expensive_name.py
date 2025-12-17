def most_expensive_name(items):
    best_name = items[0]["nome"]
    best_value = items[0]["valor"]
    for item in items:
        if item["valor"] > best_value:
            best_value = item["valor"]
            best_name = item["nome"]
    return best_name


if __name__ == "__main__":
    data = [{"nome": "Caneta", "valor": 5}, {"nome": "Livro", "valor": 40}, {"nome": "Mochila", "valor": 120}]
    print(most_expensive_name(data))
