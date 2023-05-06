
#vetor
v = [8, 6, 1, 9, 3, 4, 5]

#exibir o vetor original
for i in range(0, len(v)):
    print(v[i], " ", end="")


#ordenação por inserção
for i in range(0, len(v)):
    chave = v[i]
    j = i-1
    while((j >= 0) and (v[j] > chave)):
        v[j+1] = v[j]
        j = j - 1
    v[j+1] = chave

print()

#exibir o vetor ordenado
for i in range(0, len(v)):
    print(v[i], " ", end="")