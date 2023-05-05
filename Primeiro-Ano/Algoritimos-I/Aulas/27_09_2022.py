
import random
import sys

"""def fatorial(num):
    global x #mostra que esta e uma variavel global
    fat = 1 
    i = 2
    while(i <= num):
        fat = fat * i
        i+= 1
    return fat #expecifica o valor do subalgoritmo

x = int(input("Informe um número: "))

x1 = fatorial(x)"""

"""def fatorial2(fat):
    resultado = 1
    for i in range(fat, 0, -1):
        resultado = resultado * i
    print("Fatorial: {}".format(resultado))
fatorial2()"""

"""
Variavel Global: todo o codigo ve
Variavel Local: apenas vista dentro do subalgoritimo

Procedimento: não tem 'return', pq não tem valor
Função: Tem 'return', pq tem valor
"""

"""
val = [] * 10
menor = sys.maxsize

for i in range(0, len(val)):
    val[i] = random.randint(1, 100)
    
def menor_valor(val):

    if(val[i] < menor):
        menor = val[i]
    return menor

menor_valor(menor)"""
