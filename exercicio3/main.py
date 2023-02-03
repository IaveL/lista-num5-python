# Construa um programa que leia uma matriz 4x4 e calcule e imprima a soma da diagonal principal

matriz = []

for line in range(4):
    linha = []
    for col in range(4):
        item = int(input(f"Digite um numero para posição ({line} {col}) "))
        linha.append(item)
    matriz.append(linha)

print("Matriz: ")
for line in matriz:
    print(line)

soma_diagonal = 0

for l in range(0, len(matriz)):
    soma_diagonal += matriz[l][l]

print(f"A soma da diagonal da matriz informada acima é: {soma_diagonal}")

