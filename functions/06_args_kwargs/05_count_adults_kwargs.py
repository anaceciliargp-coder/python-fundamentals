def count_adults(**kwargs):
    adults = 0
    for name, age in kwargs.items():
        if age >= 18:
            adults += 1
    return adults


if __name__ == "__main__":
    print(count_adults(ana=31, joao=15, maria=22))
