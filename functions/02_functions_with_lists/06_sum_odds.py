def sum_odds(values):
    total = 0
    for n in values:
        if n % 2 != 0:
            total += n
    return total


if __name__ == "__main__":
    print(sum_odds([1, 2, 3, 4, 5]))
