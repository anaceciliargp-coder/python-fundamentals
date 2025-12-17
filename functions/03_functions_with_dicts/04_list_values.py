def list_values(d):
    values = []
    for k, v in d.items():
        values.append(v)
    return values


if __name__ == "__main__":
    d = {"a": 1, "b": 2, "c": 3}
    print(list_values(d))
