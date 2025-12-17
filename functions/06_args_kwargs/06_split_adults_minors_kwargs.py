def split_adults_minors(**kwargs):
    result = {"maiores": [], "menores": []}
    for name, age in kwargs.items():
        if age >= 18:
            result["maiores"].append(name.title())
        else:
            result["menores"].append(name.title())
    return result


if __name__ == "__main__":
    print(split_adults_minors(ana=31, joao=15, maria=22))
