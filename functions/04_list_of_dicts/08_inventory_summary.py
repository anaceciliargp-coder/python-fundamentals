def inventory_summary(items):
    result = {
        "total_itens": len(items),
        "total_valor": 0,
        "itens_sem_estoque": [],
        "itens_em_estoque": [],
    }

    for item in items:
        if item["quantidade"] != 0:
            result["itens_em_estoque"].append(item["nome"])
        else:
            result["itens_sem_estoque"].append(item["nome"])

        if item["valor"] != 0:
            result["total_valor"] += item["valor"]

    return result


if __name__ == "__main__":
    data = [
        {"nome": "Caneta", "valor": 5, "quantidade": 10},
        {"nome": "Caderno", "valor": 30, "quantidade": 0},
        {"nome": "Mochila", "valor": 120, "quantidade": 3},
        {"nome": "Adesivo", "valor": 0, "quantidade": 0},
        {"nome": "Livro", "valor": 40, "quantidade": 5},
    ]
    print(inventory_summary(data))
