n = 3 # Número de discos
origem = "A"
destino = "B"
auxiliar = "C"
count = 0

# Se o numero de discos for par, trocar destino e auxiliar
if n % 2 == 0:
    destino, auxiliar = auxiliar, destino

# Total de movimentos
total_movimentos = 2 **n -1

# Torres representadas como lista
torres = {
    "A": list(range(n, 0,-1)), # do disco maior para o menor
    "B": [],
    "C": []
}

# Função para mover discos
def mover(origem, destino):
    disco = torres[origem].pop()
    torres[destino].append(disco)
    print(f"Movendo disco {disco} de {origem} para {destino}")

# Algoritmo interativo
for i in range(1, total_movimentos + 1):
    print(f"movimentos: {count}")
    if i % 3 == 1:
        # movimento entre origem e destino
        if not torres[origem] or (torres[destino] and torres[destino][-1] < torres[origem][-1]):
            mover(destino, origem)
        else:
            mover(origem, destino)

    elif i % 3 == 2:
        # movimento entre origem e auxiliar
        if not torres[origem] or (torres[auxiliar] and torres[auxiliar][-1] < torres[origem][-1]):
            mover(auxiliar, origem)
        else:
            mover(origem, auxiliar)

    else:
        # movimento entre auxiliar e destino
        if not torres[auxiliar] or (torres[destino] and torres[destino][-1] < torres[auxiliar][-1]):
            mover(destino, auxiliar)
        else:
            mover(auxiliar, destino)
    count+=1
            