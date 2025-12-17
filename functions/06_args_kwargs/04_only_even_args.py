def only_even(*args):
    evens = []
    for n in args:
        if n % 2 == 0:
            evens.append(n)
    return evens


if __name__ == "__main__":
    print(only_even(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
