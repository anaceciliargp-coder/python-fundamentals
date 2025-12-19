def uppercase_long_words(words):
    return [w.upper() for w in words if len(w) > 5]

words = ["python", "java", "sol", "programacao", "lua"]
print(uppercase_long_words(words))
