"""
Loops practice: for/while.
"""

--- Validação de nota ---
nota1 = float(input("Digite a primeira nota: "))
while nota1 < 0 or nota1 > 10:
    print("Nota inválida!")
    nota1 = float(input("Digite outra nota: "))
nota2 = float(input("Digite a segunda nota: "))
while nota2 < 0 or nota2 > 10:
    print("Nota inválida!")
    nota2 = float(input("Digite outra nota: "))
media = (nota1 + nota2) / 2
print(f"MÉDIA = {media:.2f}")

--- Tabuada ---
n = int(input("Tabuada de: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
