v = [8, 3, 2, 7, 1, 5]


## Seleção ##
for i in range(0, len(v)-1):
    menor = v[i]
    i_menor = i

    for j in range(i+1, len(v)):
        if(v[j] < menor):
            menor = v[j]
            i_menor = j

    temp = v[i]
    v[i] = menor
    v[i_menor] = temp


## Inserção ##
for i in range(1, len(v)):
    valor = v[i]
    i_ant = i - 1

    while(i_ant >= 0 and v[i_ant] > valor):
        v[i_ant+1] = v[i_ant] 
        i_ant -= 1

    v[i_ant+1] = valor


## Bolha ##
for ciclos in range(0, len(v)-1):

    for i in range(0, len(v)-1):
        if(v[i] > v[i+1] ):
            temp = v[i]
            v[i] = v[i+1]
            v[i+1] = temp
    
