"""
Basics: variables, input/output, arithmetic and formatting.
Exercises: Terreno, Retângulo, Idades, Soma, Troco, Círculo, Pagamento, Consumo, Medidas, Duração.
"""

--- Terreno ---
largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
valor_m2 = float(input("Digite o valor do metro quadrado: "))
area = largura * comprimento
preco = area * valor_m2
print(f"AREA = {area:.2f}")
print(f"PRECO = {preco:.2f}")

--- Retângulo ---
import math
base = float(input("Base: "))
altura = float(input("Altura: "))
area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt(base**2 + altura**2)
print(f"AREA = {area:.4f}")
print(f"PERIMETRO = {perimetro:.4f}")
print(f"DIAGONAL = {diagonal:.4f}")

--- Duração (segundos -> hh:mm:ss) ---
duracao = int(input("Duração em segundos: "))
h = duracao // 3600
resto = duracao % 3600
m = resto // 60
s = resto % 60
print(f"{h:02d}:{m:02d}:{s:02d}")
