#-------------------------------COMEÇO-------------------------------#

# EXERCICIOS DA AULA

"""idade = int(input("Informe sua idade: "))

nome = input("Informe seu Nome: ")

sobrenome = input("Informe seu Sobrenome: ")

nome_completo = nome + " " + sobrenome

altura = float(input("Informe sua Altura: "))

peso = float(input("Informe seu Peso: "))

estudos = int(
    input("Informe quantos dias na semana você estuda Algoritimos: "))

luz = True

if luz:
    print("A luz esta acesa")
else:
    print("A luz esta apagada")

print("você tem:", idade, "anos.")
print("Seu Nome é:", nome)
print("Seu sobrenome é:", sobrenome)
print("Seu nome completo é:", nome_completo)
print("você tem", altura, "de altura.")
print("você pesa", peso, "quilos.")
print("Você estuda", estudos, "dias na semana.")
"""

"""luz = str(input("Informe luz 'apagada' ou 'acesa': "))
if luz == "acesa":
    luz_acesa = True
    
elif luz == "apagada":
    luz_apagada = False

if luz_acesa:
    print("Luz do quarto acesa")
else:
    print("Luz do quarto apagada")"""


"""luz_acesa = str(input("Informe luz apagada ou acesa: "))
if luz_acesa == "acesa":
    print("Luz do quarto acesa")
elif luz_acesa == "apagada":
    print("Luz do quarto apagada")"""
#-------------------------------FIM-------------------------------#


#-------------------------------COMEÇO-------------------------------#

#Lista de exercícios 01 - Introdução - Começo

"""print("Hello World.")

nome = input("Informe seu Nome: ")
sobrenome= input("Informe seu sobrenome: ")
idade = int(input("informe sua idade: "))
peso = float(input("informe seu peso: "))
altura = float(input("informe qual a sua altura: "))
data_de_nascimento = (input("Informe sua data de nascimento: "))
print("boas vindas",nome , sobrenome,", você tem ", idade, "anos,", ",você pesa:", peso, "quilos,", "você tem", altura, "de altura",  ",você nasceu em", data_de_nascimento)

salario = float(input("Informe seu salario:"))
aumento = input("Informe a porcentagem do aumento:").replace("%", "")
aumento = int(aumento)
salario = salario + salario * aumento/100
print("Seu novo salario é:", salario)

numero = int(input("Informe um numero inteiro: "))
antecessor = numero - 1
sucessor = numero + 1
print("numero antecessor:",antecessor , "numero sucessor:", sucessor)
"""
"""+ - * / % // **"""
"""
Lista de exercícios 01 - Introdução - Fim
"""
#-------------------------------FIM-------------------------------#




#-------------------------------COMEÇO-------------------------------#

# Lista de exercícios 02 - Começo


### EXERCICIO 1 - Faça um programa que peça um número e apresente na tela o antecessor e o sucessor dele. ###

"""numero = int(input("Informe um numero inteiro: "))
antecessor = numero - 1
sucessor = numero + 1
print("numero antecessor:", antecessor, "numero sucessor:", sucessor)"""
### EXERCICIO 1 - FIM ###


### EXERCICIO 2 - Faça um programa que peça dois números e imprima a soma deles. ###

"""n1 = int(input("Informe o primeiro numero inteiro para soma: "))
n2 = int(input("Informe o segundo numero para soma: "))
resultado_final = n1+n2
print("A soma dos numeros é", resultado_final)"""
### EXERCICIO 2 - FIM ###


### EXERCICIO 3 - Faça um programa que peça três números e imprima o produto (multiplicação) deles. ###
"""n1 = int(input("Informe o primeiro numero para multiplicação: "))
n2 = int(input("Informe o segundo numero para multiplicação: "))
n3 = int(input("Informe o terceiro numero para multiplicação: "))
mult = (n1 * n2) * n3
print("A multiplicação dos três numeros é: ", mult)"""
### EXERCICIO 3 - FIM ###


### EXERCICIO 4 - Faça um programa que peça as 4 notas bimestrais e mostre a média aritmética.###
"""n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
n3 = float(input("Informe a terceira nota: "))
n4 = float(input("Informe a quarta nota: "))
media = (n1 + n2 + n3 + n4) /4
print("A sua media final é: ", media)"""
### EXERCICIO 4 - FIM ###


### EXERCICIO 5 - Faça um programa que converta metros para centímetros.###
""""metros = int(input("informe o metro a ser convertido: "))
centimetros = metros * 100
print("o resultado é:", centimetros)"""
### EXERCICIO 5 - FIM ###


### EXERCICIO 6 - Faça um programa que peça o raio de um círculo, calcule e mostre sua área. ###
raio = float(input("informe o raio do circulo: "))
area = 3.14 * (raio ** 2)
print("A area do circulo é: ", area) 
### EXERCICIO 6 - FIM ###


### EXERCICIO 7 - Faça um programa que peça a medida do lado de um quadrado, calcule e mostre sua área. Em seguida, mostre também o perímetro do quadrado para o usuário.###
"""lado_quadrado = float(input("Informe a medida do lado do quadrado a ser calculado: "))
area = lado_quadrado * lado_quadrado
perimetro = lado_quadrado * 4
print("A área do quadrado é:", area, "é o perimetro e:", perimetro)"""
### EXERCICIO 7 - FIM ###


### EXERCICIO 8 - Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no dia. Calcule e mostre quanto você ganhou no dia e o total do seu salário em um mês (considerando 30 dias). ###
"""salario_por_hora = float(input("Informe o seu ganho por hora: "))
horas_trabalhadas = float(input("Informe quantas horas por dia você trabalha: "))
ganho_dia = salario_por_hora * horas_trabalhadas
total_salario_mes = ganho_dia * 30
print("o seu ganho diario é de: ", ganho_dia, "e o seu salario no mês é", total_salario_mes)"""
### EXERCICIO 8 - FIM ###


### EXERCICIO 9 - Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius - FORMULA - C=5 (F- 32)9 ###
"""temperatura_Farenheit = float(input("Informe a temperatura em Farenheit para o calculo:"))
temperatura_Celsius = 5*(temperatura_Farenheit - 32)/9
print("a temperatura convertida é: ", temperatura_Celsius)"""
### EXERCICIO 9 - FIM ###


### EXERCICIO 10 - Tendo como dados de entrada a altura e peso de uma pessoa, construa um algoritmo que calcule seu IMC, usando a seguinte fórmula: imc = peso ÷ altura²###
"""peso = float(input("informe o seu peso:"))
altura = float(input("informe a sua altura:"))
imc = peso/altura**2
print("o seu imc é: ",imc)"""
### EXERCICIO 10 - FIM ###


### EXERCICIO 11 - Dada a equação: ax2+bx+c=0peça para o usuário informar o valor de a, b e c e calcule: x1 =−b+b2−4ac2a x2 =−b−b2−4ac2a ###
"""
a = float(input("Informe o primeiro valor: "))
b = float(input("Informe o segundo valor: "))
c = float(input("Informe o terceiro valor: "))
delta = b**2 - 4*a*c
x1 = (-b + delta**(0.5)) / (2*a)
x2 = (-b - delta**(0.5)) / (2*a)
print("Valor de x1", x1, "Valor de x2:", x2)"""
### EXERCICIO 11 - FIM ###


### EXERCICIO 12 - Faça um programa em Python que receba o nome, o desconto (%) e o valor de um produto. Em seguida, apresente o nome, o valor atual, o desconto (em reais) e o valor final do produto da seguinte maneira:
#--------------------------------
#Produto: Nome do produto
#--------------------------------
#Desconto: R$ 00.00
#--------------------------------
#Valor final: R$ 00.00
#--------------------------------

"""nome_produto = input("Informe o nome do Produto: ")
valor_do_produto = float(input("Informe o valor do produto: "))
valor_desconto = input("Informe o valor do desconto desejado em (%): ").replace("%" ,"")
valor_desconto = float(valor_desconto)

desconto = valor_do_produto * valor_desconto/100
valor_final = valor_do_produto - desconto

print("------------------------")
print("Produto: ", nome_produto)
print("------------------------")
print("Valor do Produto: R$ ", valor_do_produto)
print("Valor do Desconto: R$ ", desconto)
print("------------------------")
print("Valor a pagar: R$ ", valor_final)
print("------------------------")"""
### EXERCICIO 12 - FIM ###


### EXERCICIO 13 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$120,00. 
# O programa deve informar ao usuário a quantidade de latas de tinta a serem compradas e o preço total.###

"""area_pintada = float("Informe a área a ser pintada em metros quadrados: ")
"""
### EXERCICIO 13- FIM ###

### EXERCICIO 14 - COMEÇO ###
ganho_por_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = float(input("Quantas horas você trabalha no mês? "))

salario_bruto = ganho_por_hora * horas_trabalhadas

imposto_de_renda = 7.5/100 * salario_bruto
inss = 8/100 * salario_bruto
sindicato = 1/100 * salario_bruto

desconto = imposto_de_renda + inss + sindicato
salario_liquido = salario_bruto - desconto

print("+ Salário Bruto: R$", salario_bruto)
print("- Imposto de Renda (7.5%): R$", imposto_de_renda)
print("- INSS (8 %): R$", inss)
print("- Sindicato (1%): R$", sindicato)
print("= Salário Líquido: R$", salario_liquido)

### EXERCICIO 14- FIM ###

#Lista de exercícios 02 - Fim

