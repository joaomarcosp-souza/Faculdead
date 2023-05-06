
#vetor
v = [8, 6, 1, 9, 3, 4, 5]

#exibir o vetor original
for i in range(0, len(v)):
    print(v[i], " ", end="")


#ordenação por bolha

#i se refere aos ciclos
#j se refere a percorrer o vetor, cada elemento.
for i in range(0, len(v)-1):
    for j in range(0, len(v)-1):
        #se o valor atual for maior que o próximo
        #troca eles de posição
        if(v[j] > v[j+1]):
            temp = v[j];
            v[j] = v[j+1]
            v[j+1] = temp

print()
#exibir o vetor ordenado
for i in range(0, len(v)):
    print(v[i], " ", end="")