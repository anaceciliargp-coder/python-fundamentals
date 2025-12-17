def date_to_hyphen(date_str):
    parts = date_str.split("/")
    day = int(parts[0])
    month = int(parts[1])
    year = int(parts[2])
    return f"{day}-{month}-{year}"


if __name__ == "__main__":
    print(date_to_hyphen("01/12/2025"))
