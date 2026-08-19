import random

# Gerar vetor aleatório com números entre 1 e 100
vetor = [random.randint(1, 100) for _ in range(10)]

print("vetor original:", vetor)

# Oedenação do vetor insert
for i in range(1, len(vetor)):
    chave = vetor[i]
    j = i - 1
    while j >= 0 and vetor[j] > chave:
        vetor[j + 1] = vetor[j]
        j -= 1
    vetor[j + 1] = chave

print("vetor ordenado:", vetor)
