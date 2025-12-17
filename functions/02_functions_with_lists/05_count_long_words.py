def count_long_words(words):
    count = 0
    for w in words:
        if len(w) > 5:
            count += 1
    return count


if __name__ == "__main__":
    print(count_long_words(["python", "java", "programação", "sol"]))
