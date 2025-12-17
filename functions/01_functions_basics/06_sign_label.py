def sign_label(n):
    if n > 0:
        return "Positivo"
    if n < 0:
        return "Negativo"
    return "Zero"


if __name__ == "__main__":
    print(sign_label(-3))
    print(sign_label(0))
    print(sign_label(9))
