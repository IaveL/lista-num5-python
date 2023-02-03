# Faça um programa que leia uma matriz 3x3 e ao final imprima a soma de seus
# elementos.

cols = int(input("Quantas colunas deseja?"))
lines = int(input("Quantas linhas deseja?"))
matriz = []
soma = 0

for l in range(1, lines + 1):
    matriz.append([])
    for c in range(1, cols + 1):
        matriz[l-1].append(float(input(f'Digite um número para a posiçao [{c}] [{l}]:')))


print(matriz)

for l in range(0, len(matriz)):
    for c in range(0, len(matriz[0])):
        soma += (matriz[l][c])


print(f'A soma dos elementos da matriz {matriz} é: {soma}')