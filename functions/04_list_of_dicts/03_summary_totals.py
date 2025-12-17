def totals(items):
    result = {"total_itens": len(items), "valor_total": 0}
    for item in items:
        result["valor_total"] += item["valor"]
    return result


if __name__ == "__main__":
    data = [{"nome": "Caneta", "valor": 5}, {"nome": "Livro", "valor": 40}, {"nome": "Mochila", "valor": 120}]
    print(totals(data))
