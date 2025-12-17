def summary_above_average_ignore_zero(items):
    result = {"total_itens": len(items), "media_valor": 0, "nomes_acima_media": []}

    total = 0
    valid_count = 0
    for item in items:
        if item["valor"] != 0:
            total += item["valor"]
            valid_count += 1

    if valid_count == 0:
        result["media_valor"] = 0
        return result

    result["media_valor"] = total / valid_count

    for item in items:
        if item["valor"] > result["media_valor"]:
            result["nomes_acima_media"].append(item["nome"])

    return result


if __name__ == "__main__":
    data = [
        {"nome": "Caneta", "valor": 5},
        {"nome": "Livro", "valor": 40},
        {"nome": "Mochila", "valor": 120},
        {"nome": "Fone", "valor": 200},
        {"nome": "Brinde", "valor": 0},
    ]
    print(summary_above_average_ignore_zero(data))
