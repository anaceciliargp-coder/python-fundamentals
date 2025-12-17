def average_values(d):
    total = 0
    for k, v in d.items():
        total += v
    return total / len(d)


if __name__ == "__main__":
    grades = {"Ana": 8, "João": 6, "Maria": 10}
    print(average_values(grades))
