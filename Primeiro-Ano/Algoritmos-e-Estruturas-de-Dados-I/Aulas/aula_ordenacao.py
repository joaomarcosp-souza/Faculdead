"""#BOLHA
[10, 30, 5, 2, 15, 8]  # 10/30
[10, 5, 30, 2, 15, 8]  # 30/5
[10, 5, 2, 30, 15, 8]  # 30/2
[10, 5, 2, 15, 30, 8]  # 30/15
[10, 5, 2, 15, 8, 30]  # 30/8
[5, 10, 2, 15, 8, 30]  # 10/5
[5, 2, 10, 15, 8, 30]  # 10/2
[5, 2, 10, 15, 8, 30]  # 10/15
[5, 2, 10, 8, 15, 30]  # 15/8
[5, 2, 10, 8, 15, 30]  # 15/30
[2, 5, 10, 8, 15, 30]  # 5/2
[2, 5, 10, 8, 15, 30]  # 5/10
[2, 5, 8, 10, 15, 30]  # 10/8

v = [10, 30, 5, 2, 15, 8]
for i in range(0, len(v)-1):
    for j in range(0, len(v)-1):
        
        if(v[j] > v[j+1]):
            temp = v[j]
            v[j] = v[j+1]
            v[j+1] = temp

#SELEÇÃO
[10, 30, 5, 2, 15, 8]
[2, 30, 5, 10, 15, 8]
[2, 5, 30, 10, 15, 8]
[2, 5, 8, 10, 15, 30]
[2, 5, 8, 10, 15, 30]
[2, 5, 8, 10, 15, 30]

v = [10, 30, 5, 2, 15, 8]
for i in range(0, len(v)-1):
    menor = v[i]
    pmenor = i
    for j in range(i+1, len(v)):
        if(menor > v[j]):
            menor = v[j]
            pmenor = j
    c = v[i]
    v[i] = menor
    v[pmenor] = c
    print(v)

#INSERÇÃO
[10, 30, 5, 2, 15, 8]
[10, 30, 5, 2, 15, 8]
[5, 10, 30, 2, 15, 8]
[2, 5, 10, 30, 15, 8]
[2, 5, 10, 15, 30, 8]
[2, 5, 8, 10, 15, 30]

v = [10, 30, 5, 2, 15, 8]

for i in range(1, len(v)):
    valor = v[i]
    j = i - 1
    while(j >= 0 and v[j] > valor):
        v[j+1] = v[j]
        j -= 1
    v[j+1] = valor
    print(v)

#busca sequencial/linear
v = [10, 30, 15, 8, 5, 2]

ivalor = -1
valor = int(input("Informe um valor para ser buscado: "))

for i in range(0, len(v)):
    if(v[i] == valor):
        ivalor = i
        break

if(valor >=0 ):
    print("Valor encontrado na posição", ivalor)
else:
    print("Valor não encontrado")
"""

#busca por BINARIO - precisa estar ordenado
v = [2,5,8,10,15,30]

ivalor = -1
valor = int(input("Valor: "))
i = 0
f = len(v)-1
while(i <= f):
    m = int((i+f)/2)
    if(v[m] == valor):
        ivalor=m
        break
    elif(valor > v[m]):
        i = m+1
    else:
        f = m-1

if(ivalor >= 0):
    print("Achou misera")
else:
    print("Achou não")

