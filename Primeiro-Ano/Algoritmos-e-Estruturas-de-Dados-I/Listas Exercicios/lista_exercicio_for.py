"""Faça um programa em Python utilizando o for (um programa pra cada um), que:
Apresente os números de 1 a 100 (um por linha).
Apresente os números de 100 a 1 (um por linha).
Apresente os números pares de 1 a 100 (um por linha).
Apresente os números ímpares de 1 a 100 (um por linha).
Faça a soma dos números de 1 a 100 e ao final mostre apenas a soma total.
Faça a soma dos números de X a Y (informados pelo usuário), desde que X seja menor que Y, e apresente o valor total (semelhante ao anterior).
Faça a multiplicação dos números de 1 a j (fatorial) e mostre o resultado final. Exemplo: Se j = 5 você deve calcular 1 * 2 * 3 * 4 * 5 = 120
"""
#A - Apresente os números de 1 a 100 (um por linha).
"""for i in range(1,101,1):
    print(i)"""
#B - Apresente os números de 100 a 1 (um por linha).
"""for b in range(100,0,-1):
    print(b)"""
#C - Apresente os números pares de 1 a 100 (um por linha).
"""for i in range(1,101):
    if(i % 2 == 0):
        print("O número, {} é par".format(i))"""
#D - Apresente os números ímpares de 1 a 100 (um por linha).
"""for i in range(1, 101):
    if(i % 2 == 1):
        print("O número, {} é impar".format(i))
"""
#E - Faça a soma dos números de 1 a 100 e ao final mostre apenas a soma total.
"""soma = 0
for i in range(1, 101):
    soma += i
    print(soma)"""
#F - Faça a soma dos números de X a Y (informados pelo usuário), desde que X seja menor que Y, e apresente o valor total (semelhante ao anterior).
"""x = int(input("Informe o primeiro valor para a soma(X): "))
y = int(input("Informe o segundo valor para a soma(Y): "))

soma = 0
if(x < y):
    for i in range(x,y+1):
        soma += i
        print(soma)
else:
    print("o valor de(X) {} e maior que o valor de(Y) {}, porfavor informe outro valor para (X).".format(x,y))"""
#G - Faça a multiplicação dos números de 1 a j (fatorial) e mostre o resultado final. Exemplo: Se j = 5 você deve calcular 1 * 2 * 3 * 4 * 5 = 120
"""j = int(input("Informe um valor fatorial: "))

calculo = 1
for i in range(1,j+1):
    calculo *= i
print(calculo)"""

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####
 

#2 - Faça um programa que leia 5 números e informe apenas o maior número.
"""maior = -99999999
for i in range(5):
    numero = int(input("Informe um número: "))
    if numero > maior:
        maior = numero
print("O maior número é: {}".format(maior))
"""
#3 - Faça um programa que leia 5 números e informe a soma e a média dos números.
"""for i in range(5):
    numero = int(input("Informe um número: "))
    soma = numero + numero + numero + numero + numero 
    media = soma/5
print("A soma dos números é de {}, e sua media e {}".format(soma,media))"""

#4 - Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
"""for i in range(1, 50+1):
    if(i % 2 == 1):
        print(i)
"""
#5 - O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu uma tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
#Lojas Quase Dois - Tabela de preços
#1 - R$ 1.99
#2 - R$ 3.98
#...
#50 - R$ 99.50
"""valor = 1.99
print("Lojas Quase Dois - Tabela de preços")
for i in range(1, 50+1):
    total = i * valor
    total = float(total)
    print("{} - R$ {}".format(i, total))"""

#6 - Utilizando o laço de repetição for, faça um programa que apresente as tabuadas do 1 ao 10 para um número informado pelo usuário.
"""numero = int(input("Informe um numero para tabuada: "))
for i in range(1, 10+1):
    tabuada = numero * i
    print("{} X {} = {}".format(numero,i,tabuada))"""

#7 - Utilizando o laço de repetição for, faça um programa que apresente as tabuadas do X a Y para um número informado pelo usuário (semelhante ao anterior, porém o usuário precisa informar três números).
"""numero = int(input("Informe um valor para tabuada: "))
x = int(input("Informe um valor para o começo da tabuada: "))
y = int(input("Informe um valor para o Fim da tabuada: "))

for i in range(x, y+1):
    tabuada = numero * i
    print("{} X {} = {}".format(numero, i, tabuada))

"""