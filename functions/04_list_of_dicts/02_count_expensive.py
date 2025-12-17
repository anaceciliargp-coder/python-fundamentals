def count_expensive(items, threshold):
    count = 0
    for item in items:
        if item["valor"] > threshold:
            count += 1
    return count


if __name__ == "__main__":
    data = [{"nome": "Livro", "valor": 40}, {"nome": "Caneta", "valor": 5}, {"nome": "Mochila", "valor": 120}]
    print(count_expensive(data, 50))
