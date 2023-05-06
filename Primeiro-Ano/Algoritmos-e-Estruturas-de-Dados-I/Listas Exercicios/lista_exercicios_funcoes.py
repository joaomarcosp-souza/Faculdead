from itertools import count
import random
#1 - Crie uma função para pedir um número inteiro ao usuário e retornar ele. Toda vez que você precisar de um número informado pelo usuário, utilize ela. Ela não tem parâmetro e o retorno é o valor digitado pelo usuário já com o tipo inteiro.
def NumeroInteiro():
    numInt = int(input("Informe um número inteiro: "))
    while(numInt < 0):
        print("Número informado {} não e valido;".format(numInt))
        numInt = int(input("Informe um novo número, dessa vez um inteiro: "))
    else:
        return(numInt)

#2 - Faça uma função para gerar números aleatórios. Esta função deve receber um número inteiro num e retornar um número aleatório entre 1 e num. Assim, toda vez que você precisar de um número qualquer pode usar a função do exercício 1 ou esta.
def NumeroAleatorio(n):
    numRand = random.randint(1, n)
    return numRand

#3 - Faça uma função que receba um número inteiro por parâmetro e retorne o mês correspondente ao número. Por exemplo, 2 corresponde a "Fevereiro". Se o número informado não corresponder a um mês (1 a 12), retorne a mensagem “Mês inválido”.
def RetornaMes(r):

    if(r == 1):
        return ("Mês de Janeiro")
    elif(r == 2):
        return ("Mês de Fevereiro")
    elif(r == 3):
        return ("Mês de Março")
    elif(r == 4):
        return ("Mês de Abril")
    elif(r == 5):
       return ("Mês de Maio")
    elif(r == 6):
        return ("Mês de Junho")
    elif(r == 7):
        return ("Mês de Julho")
    elif(r == 8):
        return ("Mês de Agosto")
    elif(r == 9):
        return ("Mês de Setembro")
    elif(r == 10):
       return ("Mês de Outubro")
    elif(r == 11):
        return ("Mês de Novembro")
    elif(r == 12):
        return ("Mês de Dezembro")
    else:
        return ("Mês invalido")

#4 - Faça funções para resolver as equações de área: do quadrado = x²  do retângulo = b . h 	(base x altura) do triângulo= (b . h)2 do trapézio = (B + b) . h2
def quadrado(x):
    qua = x * x
    return qua

def retangulo(b, a):
    ret = b * a
    return ret

def tringulo(b, a):
    tri = (b * a) /2
    return tri

def trapezio(B, b, h):
    tra = ((B + b) * h) /2
    return tra

#5 - Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que n! depende de (n-1)!; este por sua vez depende de (n-2)!; e, assim por diante, até que n seja 1, quando então tem-se que fatorial de 1 é igual a 1 mesmo. Utilize uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste número, também do tipo inteiro
def fatorial(x):
    cont = 1
    fat = 1
    while(x > cont):
        fat *= cont
        cont-=1
    return fat

#6 - Crie uma função para calcular o fatorial, mas não utilize laço de repetição.
def fatNoRepeat(n):
    if (n == 1 or n == 0):
        return (1)
    else:
        return (n * fatNoRepeat(n-1))

#7 - Faça uma função que receba um vetor como parâmetro e retorne apenas o maior valor deste vetor.
def maior(m):

    maior = m[0]
    for i in range(1, len(m)):
        if(m[i] > maior):
            maior = m[i]

        return maior

#8 - Faça uma função que receba um vetor como parâmetro e retorne apenas o menor valor deste vetor.
def menorValor(mv):

    menor = mv[0]
    for i in range(1, len(mv)):
        if(mv[i] < menor):
            menor = mv[i]

        return menor

#9 - Faça uma função para receber um vetor como parâmetro, calcular a soma desse vetor e retornar apenas a média dos valores.

def media(md):

    soma = 0
    for i in range(1, len(md)):
        soma += md[i]

    return soma/len(md)

#10 - Faça uma função que recebe um vetor de números inteiros como parâmetro. Esta função deve calcular o dobro de cada valor do vetor e retornar um vetor inteiro atualizado com o dobro de cada número. Dica: crie outro vetor dentro da função com o mesmo tamanho para preencher com o dobro. 
def calDobro(vet):
    vet2 = [0] * len(vet)
    for i in range(0,len(vet)):
        vet2[i] = vet[i] * 2

    return vet2

#11 - Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato DD de Mês Por Extenso de AAAA. Para pegar o mês por extenso, utilize a função criada no exercício 3. Por exemplo: 18/09/2019 retorna 18 de Setembro de 2019.

def recebeData(data):

    data = list(data)
    datadi = data[0] + data[1]
    datames = data[3] + data[4]
    dataAno = data[6] + data[7] + data[8] + data[9]

    return datadi + datames + dataAno
