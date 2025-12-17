def date_time_to_long(date_time_str):
    # expected: "dd/mm/aaaa hh:mm:ss" (or hh:mm)
    months = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro",
    ]
    parts = date_time_str.split(" ")
    date_part = parts[0]
    d, m, y = date_part.split("/")
    day = int(d)
    month = int(m)
    year = int(y)
    return f"{day} de {months[month - 1]} de {year}"


if __name__ == "__main__":
    print(date_time_to_long("01/01/2024 10:30:00"))
