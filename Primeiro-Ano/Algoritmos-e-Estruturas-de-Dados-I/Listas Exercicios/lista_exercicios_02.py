from dataclasses import replace
import datetime
import random
import math

"""login = input("Informe seu login:")
login = "marcos"
senha = int(input("Informe a sua senha:"))
senha = 24052022


if(login == login and senha == senha):
    print("Acesso permitido")
else:
    print("Entrada negada")
"""

"""agora = datetime.datetime.now()
hoje = agora.strftime("%d%m%Y")
hoje = int(hoje)

login = input("Informe seu login:")
login = "marcos"
senha = int(input("Informe a sua senha:"))

if(login == login and senha == hoje):
    print("Acesso permitido")
else:
    print("Acesso negado")"""

####### LISTA DE EXERCICIOS 02 - (Estrutura condicional com múltiplas alternativas (if, elif, else)) #######

## 01
"""print(" == Menu de Opções == ")
print("1. Somar 2 números")
print("2. Potência Y de um número X (xy)")
print("3. Raiz quadrada de X")
print("4. Gerar um número aleatório")
opcao = input("== Opção escolhida:")

if(opcao == "1"):
    n1 = int(input("Informe o primeiro valor:"))
    n2 = int(input("Informe o segundo valor:"))
    resultado = n1 + n2"
    print("A soma dos numeros informados é:", resultado)

elif(opcao == "2"):
    x = int(input("Informe um número: "))
    y = int(input("Informe a potencia: "))
    resultado_potencia = x**y
    print("O resultado da potencia é: ", resultado_potencia)

elif(opcao == "3"):
    numero = float(input("Informe o numero pra raiz:"))
    raiz = math.sqrt(numero)
    print("A raiz de {} é {}".format(numero, raiz))

elif(opcao == "4"):
    ale = random.randint(1,100)
    print("O numero aleatorio gerado foi:", ale)"""
##

## 02
""" 
peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: "))
imc = peso/altura**2

if(imc < 18.5):
    print("Abaixo do Peso", imc)

elif(imc > 18.5 and imc < 24.9):
    print("Peso Normal", imc)

elif(imc > 25.0 and imc < 29.9):
    print("Pré-obesidade", imc)

elif(imc > 30 and imc < 34.9):
    print("obesidade grau I", imc)

elif(imc > 35.0 and imc < 39.9):
    print("obesidade grau II", imc)

elif(imc > 40.0):
    print("obesidade grau III", imc)"""
##

## 03 
"""salario = float(input("Informe o seu salário: "))

if(salario <= 710):
    reajuste = 20

elif(salario > 710 and salario <= 1000):
    reajuste = 15

elif(salario > 1000 and salario <= 2500):
    reajuste = 10
else:
    reajuste = 5

reajuste = reajuste/100
aumento  = salario * reajuste
novo_salario = salario + aumento

print("salário antes do reajuste: ", salario)
print("percentual de aumento aplicado:",reajuste)
print("Valor do aumento:", aumento)
print("Novo salário:", novo_salario)
##"""

## 04
"""print(" == Menu de Opções == ")
print("1. Gerar um número aleatório entre X e Y")
print("2. X é par ou ímpar?")
print("3. Valor R$X com Y% de desconto")
opcao = input("== Opção escolhida:")

if(opcao == "1"):
    x = int(input("Informe o primeiro valor: "))
    y = int(input("Informe o segundo valor:" ))

    numero_ale = random.randint(x, y)
    print("Numero aléatorio gerado:", numero_ale)

elif(opcao == "2"):
    x = int(input("Informe um numero: "))

    if (x % 2 == 0):
        print("o numero {} e par".format(x))
    else:
        print("o numero {} e ímpar".format(x))

elif(opcao == "3"):

    x = float(input("Informe um valor R$:"))
    y = input("Informe o valor do desconto desejado em (%): ").replace("%", "")
    y = float(y)

    desconto = x * y/100
    valor_final = x - desconto

    print("Valor apos o desconto é de R$:",valor_final)
"""
##


## 05 

"""print("                    Até 5 Kg	         Acima de 5 Kg")
print("Morango   	R$ 8, 90 por Kg 	R$ 7, 90 por Kg  \n Maçã     	R$ 3, 90 por Kg      	R$ 3, 50 por Kg")"""

"""morangos = float(input("Informe a quantide (em Kg) de morangos comprados: "))
macas = float(input("Infome a quantide (em Kg) de maçãs compradas:"))

preco_morangos_abaixo = morangos * 8.90 
preco_morangos_acima = morangos * 7.90

preco_macas_abaixo = macas * 3.90
preco_macas_acima = macas * 3.50

if(morangos > 5):
    preco_certo_morangos = preco_morangos_acima 
else:
    preco_certo_morangos = preco_morangos_abaixo

if(macas > 5):
    preco_certo_macas = preco_macas_acima
else:
    preco_certo_macas = preco_macas_abaixo

preco_total_compra = preco_certo_macas + preco_certo_morangos

if(preco_total_compra > 25 or (morangos + macas) > 8):
    preco_final = preco_total_compra - (preco_total_compra * 7/100)
    print("Preço final:", preco_final)
else:
    print("Preço final:", preco_total_compra)"""
##

"""troco = int(input('Valor troco: '))

cem = int(troco / 100)
troco = troco - (cem*100)

cinquenta = int(troco/50)
troco = troco - (cinquenta*50)

dez = int(troco/10)
troco = troco - (dez*10)

cinco = int(troco/5)
troco = troco - (cinco*5)

um = troco

print('Notas de R$100,00 usadas = ', cem)
print('Notas de R$ 50,00 usadas= ', cinquenta)
print('Notas de R$ 10,00 usadas= ', dez)
print('Notas de R$  5,00 usadas= ', cinco)
print('Notas de R$  1,00 usadas= ', um)"""

"""troco = int(input('Valor troco: '))
notas = [100, 50, 20, 10, 5, 2, 1]

for vln in notas:

    if troco >= vln:
        qtde_notas = int(troco/vln)
        resto = int(troco - vln*qtde_notas)
        print("{} notas de R$:{} ".format(qtde_notas, vln))
        troco = resto
"""

numeroUser = int(input("escolha 2 ou 1:"))

if(numeroUser == 1 or numeroUser == 2):

    segundojogador = random.randint(1,2)
    terceirojogador = random.randint(1,2)

    print(segundojogador)
    print(terceirojogador)

    if(segundojogador == terceirojogador):
        print("O numero sorteado para o segundo e terceiro jogadores são iguais. Porfavor jogue novamente")
    elif(numeroUser == segundojogador):
        print("Você jogara com o segundo jogador")
    else:
        print("Você jogara com o terceiro jogador")

else:
    print("numero errado")
