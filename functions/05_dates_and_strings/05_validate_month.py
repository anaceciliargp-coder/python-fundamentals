def validate_month(date_str):
    parts = date_str.split("/")
    month = int(parts[1])
    if 1 <= month <= 12:
        return "Data válida"
    return "Data inválida"


if __name__ == "__main__":
    print(validate_month("17/12/2025"))
    print(validate_month("17/13/2025"))
