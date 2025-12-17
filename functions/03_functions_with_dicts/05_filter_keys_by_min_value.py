def filter_keys_by_min_value(d, minimum):
    selected = []
    for k, v in d.items():
        if v >= minimum:
            selected.append(k)
    return selected


if __name__ == "__main__":
    salaries = {"Ana": 5000, "João": 2500, "Maria": 3200}
    print(filter_keys_by_min_value(salaries, 3000))
