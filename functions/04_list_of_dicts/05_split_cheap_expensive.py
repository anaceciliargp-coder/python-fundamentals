def split_cheap_expensive(items, threshold):
    result = {"baratos": [], "caros": []}
    for item in items:
        if item["valor"] <= threshold:
            result["baratos"].append(item["nome"])
        else:
            result["caros"].append(item["nome"])
    return result


if __name__ == "__main__":
    data = [{"nome": "Caneta", "valor": 5}, {"nome": "Livro", "valor": 40}, {"nome": "Mochila", "valor": 120}]
    print(split_cheap_expensive(data, 50))
