def count_greater_than_10(*args):
    count = 0
    for n in args:
        if n > 10:
            count += 1
    return count


if __name__ == "__main__":
    print(count_greater_than_10(3, 15, 8, 22))
