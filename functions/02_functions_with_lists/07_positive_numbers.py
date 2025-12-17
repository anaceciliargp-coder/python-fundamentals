def positive_numbers(values):
    positives = []
    for n in values:
        if n > 0:
            positives.append(n)
    return positives


if __name__ == "__main__":
    print(positive_numbers([-2, 5, 0, -1, 8, 3]))
