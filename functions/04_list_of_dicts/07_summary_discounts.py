def summary_with_discounts(items):
    result = {
        "total_itens": len(items),
        "total_pago": 0,
        "total_descontos": 0,
        "nomes_com_desconto": [],
    }

    for item in items:
        if item["valor"] != 0:
            result["total_pago"] += item["valor"]
            if "desconto" in item:
                result["total_descontos"] += item["desconto"]
                result["nomes_com_desconto"].append(item["nome"])

    return result


if __name__ == "__main__":
    data = [
        {"nome": "Caneta", "valor": 5},
        {"nome": "Livro", "valor": 40, "desconto": 0.25},
        {"nome": "Mochila", "valor": 120, "desconto": 0.10},
        {"nome": "Fone", "valor": 200},
        {"nome": "Brinde", "valor": 0, "desconto": 0.50},
    ]
    print(summary_with_discounts(data))
