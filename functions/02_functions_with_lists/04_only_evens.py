def only_evens(values):
    evens = []
    for n in values:
        if n % 2 == 0:
            evens.append(n)
    return evens


if __name__ == "__main__":
    print(only_evens([1, 2, 3, 4, 5, 6]))
