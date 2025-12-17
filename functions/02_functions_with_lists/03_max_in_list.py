def max_in_list(values):
    biggest = values[0]
    for n in values:
        if n > biggest:
            biggest = n
    return biggest


if __name__ == "__main__":
    print(max_in_list([1, 4, 5, 8, 14, 33, 99, 101, 2, 45]))
