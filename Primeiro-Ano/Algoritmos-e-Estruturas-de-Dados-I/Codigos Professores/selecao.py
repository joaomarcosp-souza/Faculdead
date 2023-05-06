
#vetor
v = [8, 6, 1, 9, 3, 4, 5]

#exibir o vetor original
for i in range(0, len(v)):
    print(v[i], " ", end="")


#ordenação por seleção
for i in range(0, len(v) - 1):
    i_menor = i
    for j in range(i+1, len(v)):
        if(v[j] < v[i_menor]):
            i_menor = j
    menor = v[i_menor]
    v[i_menor] = v[i]
    v[i] = menor

print()

#exibir o vetor ordenado
for i in range(0, len(v)):
    print(v[i], " ", end="")