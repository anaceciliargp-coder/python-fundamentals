def date_to_long_ptbr(date_str):
    months = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro",
    ]
    parts = date_str.split("/")
    day = int(parts[0])
    month = int(parts[1])
    year = int(parts[2])
    return f"{day} de {months[month - 1]} de {year}"


if __name__ == "__main__":
    print(date_to_long_ptbr("17/12/2025"))
