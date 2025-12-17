def info(name, language="pt"):
    if language == "en":
        return f"Hello, {name}!"
    return f"Olá, {name}!"


if __name__ == "__main__":
    print(info("Ana", language="en"))
    print(info("Ana"))
