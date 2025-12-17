def extract_year(date_str):
    parts = date_str.split("/")
    year = int(parts[2])
    return year


if __name__ == "__main__":
    print(extract_year("17/12/2025"))
