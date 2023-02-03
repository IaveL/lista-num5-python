# Escreva um programa que leia uma matriz 3x3, armazene em um vetor a soma dos
# elementos por linha e exiba a matriz e o vetor de soma
matriz = []
somas_vetor = []

for l in range(3):
    linha = [] # inicializa a linha
    soma_linha = 0
    for c in range(3):
       item = ((int(input(f"Digite o item ({l} {c}): "))))
       linha.append(item)
       soma_linha += item
    matriz.append(linha)
    somas_vetor.append(soma_linha)
   
# +=

# print(f'A soma é {soma}')
print("Matriz:")
for line in matriz:
    print(line)
print(f'Vetor soma é: {somas_vetor}')
#######################################################
