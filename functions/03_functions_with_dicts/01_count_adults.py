def count_adults(people_ages):
    adults = 0
    for name, age in people_ages.items():
        if age >= 18:
            adults += 1
    return adults


if __name__ == "__main__":
    data = {"Ana": 31, "João": 15, "Maria": 22}
    print(count_adults(data))
