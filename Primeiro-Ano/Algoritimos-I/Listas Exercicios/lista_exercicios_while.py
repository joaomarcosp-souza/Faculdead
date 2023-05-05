import math
import random
import sys
import time
from ast import Num

# 1 - Faça algoritmos em Python, utilizando o while, que:
    #A - Apresente na tela os números de 1 a 100.

"""num = 1
while(num <= 100):
    print(num)
    num+=1"""

    #B - Faça a soma dos números de 1 a 100 e apresente somente o resultado.

"""num = 0
soma = 0
while(num < 100):
    num+=1
    soma += num
print(soma)
"""
    #C - Apresente na tela somente os números pares entre 50 e 100.

"""num = 50
while(num <= 100):
    if(num %2 == 0):
        print(num)
    num+=1"""
    
    #D - Apresente na tela somente os números ímpares entre 1 e 50.

"""num = 0
while(num <= 50):
    if(num %3 == 0):
        print(num)
    num+=1"""
    #E - Apresente na tela somente a soma dos números pares entre 1 e 100

"""num = 0
soma = 0
while(num <= 100):
    if(num %2 == 0):
        soma += num
    num+=1
print(soma)"""

    #F - Apresente na tela os números de X a Y (peça para o usuário informar os valores de X e de Y).

"""x = int(input("Informe o valor de X: "))
y = int(input("Informe o valor de Y: "))

if(x < y):
    while(x <= y):
        print(x)
        x+=1
elif(y < x):
    while(y <= x):
        print(y)
        y+=1
else:
    print("Os numeros Informados são iguais")"""

    #G - Faça a soma dos números de X a Y e apresente somente o resultado (peça para o usuário informar os valores de X e de Y).

"""x = int(input("Informe o valor de X(Inicio): "))
y = int(input("Informe o valor de Y(Fim): "))

soma = 0
if(x < y):
    while(x <= y):
        soma += x
        x+=1
elif(y < x):
    while(y <= x):
        soma += y
        y+=1
print(soma)"""

    #H - Apresente na tela somente os números ímpares entre X e Y (peça para o usuário informar os valores de X e de Y).

"""x = int(input("Informe um valor para X: "))
y = int(input("Informe um valor para y: "))

if(x < y):
    while(x <= y):
        if(x % 2 == 0):
            print(x)
        x+=1
elif(y < x):
    while(y <= x):
        if(y % 2 == 0):
            print(y)
        y+=1
else:
    print("Valores Iguais")"""

#2 - Faça um programa para calcular a tabuada:
    #B - do X ao Y para um número informado pelo usuário (o usuário também deve informar os valores de X e Y).

"""
num = int(input("Informe a tabuda desejada: "))
x = int(input("Informe um valor para  o começo da tabuada: "))
y = int(input("Informe um valor para  o fim da tabuada: "))

if(x < y):
    while(x <= y):
        resultado = num * x
        print("{} X {} = {}".format(num,x,resultado))
        x+=1
elif(y < x):
    while(y <= x):
        resultado = num * y
        print("{} X {} = {}".format(num,y, resultado))
        y += 1
else:
    resultado = num * x
    print("{} X {} = {}".format(num, x, resultado))
    x += 1"""

#3 - Na matemática, o fatorial de um número natural n, representado por n!, é o produto de todos os inteiros positivos menores ou iguais a n. Por exemplo: o fatorial de 5 é representado por 5! que é igual a 5 x 4 x 3 x 2 x 1. Faça um programa que peça um número para o usuário e apresente na tela seu fatorial.

"""n = int(input("Informe um para o fatorial: "))
p = 1
calculo = 1
while(p <= n):
    calculo*=p
    print("{} x {} = {}".format(n, p, calculo)) 
    p+=1"""

#4 - Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, faça um programa que peça ao usuário qual o termo final(N) e calcule o valor de H.

"""n = int(input("Informe o termo final(N): "))
h = 0
num = 1
while(num <= n):
    h += 1/num
    print(h)
    num+=1"""

#5 - Faça um programa em Python “Acertou, ganhou!” o programa deverá:
#A - Gerar um número aleatório entre 1 e 10 e pedir para o usuário digitar números até que acerte. Ao acertar, apresente uma mensagem parabenizando e finalize o programa.

"""num = 0
qtde = 0
ale = 1
while(num != ale):
    ale = random.randint(1,10)
    num = int(input("Digite um número: "))
    print("Número gerado: {}, Seu numero: {}".format(ale, num))
    qtde +=1
print(" GANHOUUU! \n Você precisou de {} tentativas para acertar \n Finalizando o jogo...".format(qtde))
"""

#6 - Faça um programa que mostre o menu a seguir, receba a opção do usuário e os dados necessários para executar cada operação. O programa será executado repetidamente até que o usuário passe o número informado para sair do programa(opção).

"""opc = 0
while(opc != 4):

    print("\n== == == Menu Principal == == == \n 1. Par ou ímpar? \n 2. Potência X elevado a y \n 3. Raiz quadrada \n 4. Sair.")
    opc = int(input("\n Escolha uma opção: "))
    print(" ")

    if(opc == 1):
        num = int(input("Informe um número para verificação: "))
        if(num %2 == 0):
            print("O número informado {}, é par.".format(num))
        else:
            print("O número informado {}, é ímpar.".format(num))

    elif(opc == 2):
        x = int(input("Informe o valor de X: "))
        y = int(input("Informe o valor de Y(que será elevado a X): "))
        resultado = x**y
        print("Resultado: {} ".format(resultado))

    elif(opc == 3):
         num = int(input("Informe um valor para a raiz: "))
         raiz = math.sqrt(num)
         print("A raiz de {} é {}.".format(num, raiz))

    elif(opc == 4):
        print("Finalizando o programa...")

    else:
        print("Número Informado é invalido;")"""
    
#7 - Faça um programa que mostre o menu a seguir, receba a opção do usuário e os dados necessários para executar cada operação. O programa será executado repetidamente até que o usuário passe o número informado para sair do programa(opção).

"""opc = 0
while(opc != 4):
    print(" \n == == == Menu Principal == == == \n 1. Fazer a tabuada do 1 ao 10 para um número X \n 2. Apresentar os múltiplos de X entre 1 e 100 \n 3. Apresentar a soma dos números de 1 a 100 \n 4. Sair do programa")

    opc = int(input("\n Escolha uma opção: "))

    if(opc == 1):
        numero = int(input("Informe um número para a tabuada: "))
        cont = 1
        while(cont <= 10):
            resultado = numero * cont
            print("{} X {} = {}".format(numero, cont, resultado))
            cont+=1

    elif(opc == 2): 
        numero = int(input("Informe o valor de X: "))
        cont = 1
        print("Números multiplos de {} são: ".format(numero))
        while(cont <= 100):
            if(cont %numero == 0):
                print("{}".format( cont))
            cont+=1

    elif(opc == 3):
        cont = 0
        soma = 0
        while(cont <= 100):
            soma += cont
            cont +=1
        print("A soma do números de 1 a 100 é de: {}.".format(soma))
    
    elif(opc == 4):
        print("Finalizando o programa...")

    else:
        print("Opção Invalida")
"""

#8 - O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agorapossui uma loja de conveniências. Faça um programa que implemente uma caixa registradora. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. O valor “0” (zero) deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. A saída deve ser conforme o exemplo abaixo:

"""valor = 1
qtde = 1
total = 0
print("Informe zero(0) para finalizar a compra.")
while(valor != 0):
    valor = float(input("Produto {}: R$ ".format(qtde)))
    total += valor
    qtde += 1

print("Total: R$ ", total)
dinheiro = int(input("Dinheiro: R$ "))
troco = dinheiro - total
print("Troco: R$ ", troco)
"""

#9 - O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia sete temperaturas, e informe ao final a menor e a maior temperatura, além da média das temperaturas.

"""cont = 1
maior = -999999999999999999999999
menor = 9999999999999999999999999
media = 0
soma = 0
while(cont <= 7):
    temperatura = int(input("Informe a temperatura: "))
    
    if(temperatura > maior):
        maior = temperatura
    elif(temperatura < menor):
        menor = temperatura
    
    soma = soma + temperatura
    media = soma/7
    
    cont+=1
    
print(" Maior: {} \n Menor: {} \n Media: {}".format(maior, menor, media))
"""

# 10 - Faça um programa que calcule e mostre a média aritmética de N notas informadas pelo usuário. O programa pode parar de pedir notas quando o usuário informar -1, por exemplo.

"""cont = 1
nota = 0
soma = 0
print("Informe um número negativo para parar o programa.")
while(nota >= 0):
    
    nota = int(input("Informe o valor da {}º nota: ".format(cont)))
    soma = soma + nota
    media = soma / cont
    
    cont+=1

print("Finalizando o programa...")
media = int(media)
print("Media: ",media)"""

#11 - ) Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor pago em cada um. 

"""cds = int(input("Informe a quantidade de CDs que você possui: "))

cont = 1
total = 0
media = 0
falta = cds
while(cont <= cds):


    valor_cds = float(input("Informe o valor do {}º CD:  ".format(cont)))
    print("Faltam {} CDs para acabar.".format(falta))
    total = total + valor_cds
    media = total/cont

   
    falta -= 1
    cont+=1

print("Total gasto nos CDs: {}".format(total))
print("Media gasta por CD: {}".format(media))"""


#12 - Uma academia deseja fazer um questionário entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
#Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
"""cont = 1
codigo = 1

soma_peso = 0
soma_altura = 0

codigo_mais_magro = 0
codigo_mais_gordo = 0

codigo_mais_alto = 0
codigo_mais_baixo = 0

mais_alto = -sys.maxsize-1
mais_baixo = sys.maxsize

mais_gordo = -sys.maxsize-1
mais_magro = sys.maxsize

while(codigo != 0):

    codigo = int(input("Informe seu código: "))
    if(codigo == 0):
        break
    altura = float(input("Informe a sua altura: "))
    peso = float(input("Informe seu peso: "))

    soma_altura += altura
    soma_peso += peso

    if(altura > mais_alto):
        mais_alto = altura
        codigo_mais_alto = codigo
    elif(altura < mais_baixo):
        mais_baixo = altura
        codigo_mais_baixo = codigo

    if(peso > mais_gordo):
        mais_gordo = peso
        codigo_mais_gordo = codigo
    elif(peso < mais_magro):
        mais_magro = peso
        codigo_mais_magro = codigo

    cont += 1
    
media_altura = soma_altura/cont
media_peso = soma_peso/cont

print(" ")
print("Dados do cliente mais alto:\n  Código: {}, Altura: {}.".format(codigo_mais_alto,mais_alto))
print("Dados do cliente mais baixo:\n Código: {}, e sua altura: {}.".format(codigo_mais_baixo, mais_baixo))
print(" ")
print("Dados do cliente mais gordo:\n Código: {}, Peso: {}.".format(codigo_mais_gordo,mais_gordo))
print("Dados do cliente mais magro:\n Código: {}, Peso: {}.".format(codigo_mais_magro, mais_magro))
print(" ")
print("Media das alturas: ", float(media_altura))
print("Media dos pesos: ", int(media_peso))"""


#13 - Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição cima informada(retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
"""maior = -sys.maxsize-1
menor = sys.maxsize

media = 0
soma = 0

cont = 1
notas = []

nome = input("Nome Atleta: ")
while(cont <= 7):
    
    nota = float(input("{}º nota: ".format(cont)))
    notas.append(nota) #Posiciona o novo valor na ultima posição do vetor

    if(nota > maior):
        maior = nota
    elif(nota < menor):
        menor = nota

    cont+=1

notas.remove(max(notas))
notas.remove(min(notas))

media = sum(notas) /len(notas) #Sum: Soma os valores dentro do vetor e retorna o inicio caso não for especificado um valor de incio ele será zero padrão, len conta a quantidade de valores no vetor

print(" ")
print("Resultado final: ")
print("Atleta: {} \n Melhor nota: {} \n Pior nota: {} \n Media: {}".format(nome, maior, menor, round(media,2)))

"""

#14- Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de crescimento de 3 % e que a população de B seja 200.000 habitantes com uma taxa de crescimento de 1.5 % . Faça um programa que calcule e apresente o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento de cada um.

"""a = 80000
b = 200000
ano = 0

while(a <= b):
    a = a + (a * 0.03)
    b = b + (b* 0.015)

    ano+=1
print("O país A ultrapassou o país B depois de: {} anos".format(ano))
"""

# 15 - Desafio sem usar strings: faça um programa que peça para o usuário informar um número entre 1 e 999. Em seguida, apresente esse número invertido.
"""
numero = 0
numero_inverso = 0

while(numero <= 0):

if(numero == 0):
        break

"""
"""numero = int(input("Informe um número: "))
original = numero
if(numero >= 1 and numero <= 999):
    while(numero > 0): 
        num = numero % 10
        numero_inverso = (numero_inverso * 10) + num
        numero = numero // 10
    print("O numero reverso de {} fica: {}".format(original,numero_inverso))
else: 
    print("Número invalido...")"""

""" num = int(input("Informe um número entre 1 e 999: "))
    lista = [int(x) for x in str(num)]
    lista.append(num)
    lista.reverse()
    print(lista)
    print("Numero original: {}, reverso: {}".format(num, lista))
    time.sleep(3)"""


#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

"""nota = int(input("Informe uma nota entre 0 e 10: "))
while(nota < 0 or nota > 10):
    nota = int(input("Eu já disse, informe uma nota entre 0 e 10: "))
print("Número informado {}".format(nota))
"""

#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

"""nome = input("Informe o usuario: ")
senha = input("Informe a senha: ")
while(nome == senha):

    print("\nUsuário igual a Senha!\n")
    senha = input("Informe uma nova senha: ")
    if(senha != nome):
        repita_a_senha = input("Informe a senha novamente: ")
        while(repita_a_senha != senha):
            print("\n As senhas são diferentes!\n")
            repita_a_senha = input("Informe a senha novamente: ")

print("Logando...")"""

# Faça um programa que leia e valide as seguintes informações: Nome: maior que 3 caracteres Idade: entre 0 e 150 Salário: maior que zero Sexo: 'f' ou 'm' Estado Civil: 's', 'c', 'v', 'd'

"""nome = input("Informe um nome maior que 3 caracteres: ")
while(len(nome) <= 3):
    print("\n Nome informado e menor que 3 caracteres.\n")
    nome = input("Informe um nome maior que 3 caracteres: ")

idade = int(input("Informe uma idade: "))
while(idade >= 150 or idade <= 0):
    print("\n Idade invalida\n")
    idade = int(input("Informe uma idade: "))

salario = float(input("Informe o seu salario: "))
while(salario <= 0):
    print("\nsalario informado e menor ou igual a 0")
    salario = float(input("Informe o seu salario: "))

sexo = input("Informe o seu sexo: 'f' ou 'm': ")
while(sexo != 'f' or sexo != 'm'):
    print("\ngenero  invalido.")
    sexo = input("Informe o seu sexo: 'f' ou 'm': ")
    if(sexo == 'f' or sexo == 'm'):
        break

estado_civil = input("Informe o seu estado civil: 's', 'c', 'v', 'd': ")
while(estado_civil != 's' or estado_civil != 'c' or estado_civil != 'v' or estado_civil != 'd'):
    print("\nestado civil invalido.")
    estado_civil = input("Informe o seu estado civil: 's', 'c', 'v', 'd': ")
    if(estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd'):
        break

print("Todos os dados foram validados:\n")
print("Nome: {}\nIdade: {}\nSalario: {}\nSexo: {}\nEstado Civil: {}".format(nome,idade,salario,sexo,estado_civil))"""

#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

"""a = 80000
b = 200000
ano = 0
while(a <= b):

    a = a + (a * 0.03)
    b = b + (b * 0.015)

    ano += 1
print("Foi preciso {} anos para o país A ultrapassar o B.".format(ano))"""

#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
"""
pais_a = int(input("Informe a população do País 'A': "))
taxa_a = float(input("Informe a taxa anual de crescimento do País 'A': "))

pais_b = int(input("Informe a população do País 'B': "))
taxa_b = float(input("Informe a taxa anual de crescimento do País 'B': "))

opc = 1
ano = 0
while(pais_a <= pais_b):

    pais_a = pais_a + (pais_a * taxa_a/100)
    pais_b = pais_b + (pais_b * taxa_b/100)

    ano+=1

print("Será preciso {} anos para o país A ultrapassar o B.".format(ano))"""

#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.
"""
cont = 1
while(cont <= 20):
    print(cont)
    cont +=1
print(list(range(cont)))
"""

#Faça um programa que leia 5 números e informe o maior número.
"""cont = 1
maior = -sys.maxsize-1
while(cont <= 5):
    num = int(input("Informe o {}º número: ".format(cont)))
    if(num >= maior):
        maior = num
    cont+=1

print("O maior número informado foi {}".format(maior))"""

#Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
cont = 1
soma = 0
media = 0
while(cont <= 5):
    numero = int(input("Informe o valor do {}º número: ".format(cont)))

    soma += numero
    media = soma/cont

    cont+=1
print("A soma dos número é: {}, e a sua media é {}".format(soma,media))"""

#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
"""cont = 1
while(cont <= 50):
    if(cont % 2 == 0):
        print("Os números pares são: {}".format(cont))

    cont+=1"""

#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
"""
x = int(input("Informe o número de inicio: "))
y= int(input("Informe o número de enceramento: "))

cont = 0
soma = 0
if(x >= 0 and y >= 0):
    if(x < y):
        while(x <= y):
            print(x)
            soma = soma + x
            x += 1
        print(soma)
    elif(y < x):
        print(y)
        while(y <= x):
            soma = soma + y
            y += 1
else:
    print("Os numeros Informados são iguais")"""
    
#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:

"""tabuada = int(input("tabuada de: "))
comeco = int(input("Começo da Tabuada: "))
fim = int(input("Fim da Tabuada: "))

print("Vou montar a  tabuada do {} começando em {} e terminando em {}: \n".format(tabuada,comeco,fim))
while(comeco <= fim):

    resultado = tabuada * comeco
    print("{} X {} = {}".format(tabuada,comeco,resultado))

    comeco +=1"""

#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

"""base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = 1

cont = 0
while(cont <= expoente):

    resultado = base * base
    resultado = base * resultado

    cont+=1

print(resultado)"""

#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
"""cont = 1
pares = 0
impar = 0

while(cont <= 10):

    numero = int(input("Informe o {}º número: ".format(cont)))
    if(numero % 2 == 0):
        pares +=1
    else:
        impar +=1
    cont+=1

print("Quantidade de números pares é {}".format(pares))
print("Quantidade de números impares é {}".format(impar))"""

# série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

"""ultimo = 1
penultimo = 1
count = 1
print(ultimo)
print(penultimo)
while(count <= 9):
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    count += 1
    print(termo)"""

#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

"""ultimo = 1
penultimo = 1
print(ultimo)
print(penultimo)
termo = 0

while(termo < 500):
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    if(500 >= termo):
        print(termo)"""
    
#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

"""numero = int(input("Informe um número para o fatorial: "))
cont = 1
fatorial = 1
while(cont <= numero):
    fatorial *= cont
    print("{} x {} = {}".format(numero, cont, fatorial))
    cont += 1"""

#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""numero = 1
cont = 1
maior = -sys.maxsize-1
menor = sys.maxsize

numero = int(input("Informe o {}º número entre 0 é 1000: ".format(cont)))
while(numero <= 0 or numero >= 1000):
    numero = int(input("Informe o {}º número entre 0 é 1000: ".format(cont)))

    while(numero > 0):
        if(numero == 0):
            break

        if(numero > maior):
            maior = numero
        elif(numero < menor):
            menor = numero

        soma = menor + maior

        cont += 1
print("Maior valor: {}".format(maior))
print("Menor valor: {}".format(menor))
print("Soma dos valores: {}".format(soma))"""


"""soma = 0
impar = 0
cont = 1
for i in range(1, 5+1):
    numero = int(input("Numero: "))
    if(numero % 3 == 0):
        impar = numero
        soma = soma + impar
        media = soma/cont
        cont +=1

print("Media: ", media)
"""

"""
salgado = 3.90
bauru = 6.00
bauru_ovo = 7.00
burguer = 8.50
refrigerante = 3.50
suco = 4.50

somar = 0
lista = []

valor_pedido = 1

codigo = 1

print("Informe 0 para sair do programa.")

while(codigo != 0):
    codigo = 1
    print("O cardápio da lanchonete é o seguinte: \n Especificação - Código - Preço \nSalgado - 100 - R$3, 90 \nBauru Simples - 101 - R$6, 00 \nBauru com ovo - 102 - R$7, 00 \nX-burguer - 103 - R$8, 50 \nRefrigerante - 104 - R$3, 50 \nSuco - 105 - R$4, 50")
    codigo = int(input("Codigo produto: "))
    if(codigo == 0):
        break
    if(codigo >= 100 and codigo <= 105):
        quantidade = int(input("Quantidade: "))
        if(codigo == 100):
            valor_pedido = quantidade * salgado 
        elif(codigo == 101):
            valor_pedido = quantidade * bauru
        elif(codigo == 102):
            valor_pedido = quantidade * bauru_ovo
        elif(codigo == 103):
            valor_pedido = quantidade * burguer
        elif(codigo == 104):
            valor_pedido = quantidade * refrigerante
        elif(codigo == 105):
            valor_pedido = quantidade * suco
        else:
            print("Código de produto invalido...")
        somar = somar + valor_pedido
    else:
        print("Codigo invalido...")
print("Total: ",somar)"""

salario = int(input("Informe o salario: "))

descontoinns = (salario * 0.085)
dentonto = (salario * 0.05)

salariofim = salario - descontoinns - descontoinns

print(salariofim)