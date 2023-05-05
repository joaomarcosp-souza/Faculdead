"""Crie procedimentos com parâmetros informados pelo usuário no programa principal:
Faça uma procedimento que soma dois números. Deve ser utilizado um procedimento chamado somar(), que deve receber os números a serem somados, somar os números e apresentar o resultado na tela.
Faça um procedimento que multiplica dois números. Deve ser utilizado um procedimento chamado multiplicar(), que deve receber os números e realizar a operação de multiplicação, apresentando o resultado na tela.
Faça um procedimento que calcule a raiz quadrada de um número chamado calcularRaiz(). O procedimento deve receber o número por parâmetro, efetuar o cálculo e apresentar o resultado.
Faça um procedimento que calcule a potência de um número (XY) chamado calcularPotencia(). O procedimento deve receber os números por parâmetro, efetuar o cálculo e apresentar o resultado.
Faça um procedimento que calcule a tabuada de 1 a 10 para um número chamado calcularTabuada(). O procedimento deve receber o número por parâmetro, efetuar o cálculo e apresentar o resultado.
"""

import math
import random
import sys
"""
def somar(a, b):
    somar = n1 + n2
    print("A soma dos números {} + {}  fica: {}".format(a, b, somar))

def multiplicar(x, y):
    resultado =  n1 * n2
    print("A multiplicação dos números {} x {} fica: {}".format(x, y, resultado))

def calcularRaiz(d):
    raiz = math.sqrt(n1)
    print("A raiz de {} fica: {}".format(d, raiz))

def calcularPotencia(e, f):
    potencia = math.pow(b, p)
    print("A pôtencia de {}^{} fica: {}".format(e, f, potencia))

def calcularTabuada(g):

    for i in range(1, 10+1):
        tabuada = numero * i
        print("{} X {} = {}".format(g, i, tabuada))

opc = 0
while(opc != 6):
    print(" \n == == == Menu Principal == == == \n 1. Somar \n 2. Multiplicar \n 3. Calcular Raiz \n 4. Calcular Potencia \n 5. Calcular Tabuada \n 6. Sair")

    opc = int(input("Informe a opção: "))

    if(opc == 1):
        print("Submenu 'Somar'")
        n1 =  int(input("Informe o valor do primeiro número para soma: "))
        n2 = int(input("Informe o valor do segundo número par asoma: "))
        somar(n1, n2)

    elif(opc == 2):
        print("Submenu 'Multiplicação'")
        n1 = int(input("Informe o primeiro número para multiplicação: "))
        n2 = int(input("Informe o segundo número para multiplicação: "))
        multiplicar(n1, n2)
    
    elif(opc == 3):
        print("Submenu 'Calcular Raiz'")
        n1 = int(input("Informe o valor: "))
        calcularRaiz(n1)
    
    elif(opc == 4):
        print("Submenu 'Calcular Potência'")
        b = int(input("Informe o valor da Base: "))
        p = int(input("Informe o valor do expoente: "))
        calcularPotencia(b, p)

    elif(opc == 5):
        print("Submenu 'Calcular Tabuada'")
        numero = int(input("Informe o número da tabuada: "))
        calcularTabuada(numero)
    
    elif(opc == 6):
        print("Finalizando o programa...")
        break
    else:
        print("Número Informado é invalido;")
"""

def imprimirVetor(a):
    for i in range(1, a+1):
        vet = random.randint(1, 100)
        print("{}º - {}".format(i, vet))

def acharmenor(b):
    maior = -sys.maxsize
    for i in range(1, b+1):
        vet = random.randint(1, 150)
        if(vet > maior):
            maior = vet
    print("Maior número: {}".format(maior))

def acharmaior(c):
    menor = sys.maxsize+1
    for i in range(1, c+1):
        vet = random.randint(1, 200)
        if(vet < menor):
            menor = vet
    print("Menor número: {}".format(menor))


opc = 0
while(opc != 4):
    print(" \n == == == Menu Principal == == == \n 1. Imprimir Vetor \n 2. Achar Maior \n 3. Achar Menor \n 4. Sair")
    opc = int(input("Informe a opção: "))

    if(opc == 1):
        print("Submenu 'Imprimir Vetor'.")
        tam = int(input("Informe o  tamanho do vetor: "))
        vet = [] * tam
        imprimirVetor(tam)
        
    elif(opc == 2):
        print("Submenu 'Achar Menor'.")
        tam = int(input("Tamanho do Vetor: "))
        ve = [] * tam
        acharmenor(tam)
        
    elif(opc == 3):
        print("Submenu 'Achar Maior'.")
        tam = int(input("Informe qual será o tamanho do vetor: "))
        v = [] * tam
        acharmaior(tam)
       
    elif(opc == 4):
        print("Finalizando o programa...")
        break
    else:
        print("Número Informado é invalido;")

