def list_keys(d):
    keys = []
    for k, v in d.items():
        keys.append(k)
    return keys


if __name__ == "__main__":
    d = {"a": 1, "b": 2, "c": 3}
    print(list_keys(d))
