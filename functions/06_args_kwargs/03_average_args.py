def average(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)


if __name__ == "__main__":
    print(average(3, 15, 8, 22))
