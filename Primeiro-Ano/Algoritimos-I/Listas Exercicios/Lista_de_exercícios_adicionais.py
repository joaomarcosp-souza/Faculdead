
import math
import random

# 10 - Implemente um programa que seja capaz de calcular e apresentar ao usuário a área de um círculo. Sabe-se que para calcular a área de um círculo utiliza-se a fórmula A=R2onde A é a área do círculo e R é o raio. Solicite ao usuário pelos dados necessários. Utilize a biblioteca matemática (math) para se obter o valor exato de .
"""r = float(input("Informe o raio do circulo: "))
a = math.pi * (r**2)
print(a)"""

# 12 - Sabe-se que as variáveis x=10, y=20 e z=30. Desenvolva um algoritmo que, atribuindo-se os valores às variáveis, consiga realizar a troca dos valores, de forma que x receba o valor de z, y receba o valor de x e z receba o valor de y. Apresente ao usuário os valores de x, y e z antes da troca e depois da troca.
"""
x = 10
y = 20
z = 30
print("antes", x)
print("antes", y)
print("antes", z)

x = z
y = x
z = y

print("Depois",x)
print("Depois",y)
print("Depois",z)"""
# 13 - Implemente um programa que solicite ao usuário pelo dia, mês e ano no formato ddmmaa e apresente na tela o dia informado, o mês informado e o ano informado. Exemplo: data=100219. Dia: 10, Mês: 02 e Ano:19. Para o cálculo, utilize apenas os operadores / e %, convertendo os resultados sempre para inteiro).


# 14 - Crie um programa que solicite ao usuário por um número. Apresente na tela a terça parte deste número (⅓ dele).
"""
num = int(input("Informe um numero: "))
terco = num/3
print(terco)
"""
# 15 - Um programa deve receber 4 números indicando as notas de um aluno em uma disciplina. Sabe-se que cada avaliação possui um peso na média final, sendo que a primeira nota possui peso 1, a segunda nota possui peso 3, a terceira nota possui peso 2 e a quarta nota possui peso 4. Implemente um programa que calcule a média ponderada do aluno e apresente-a na tela.
"""valor1 = float(input("Informe o valor da primeira nota: "))
valor2 = float(input("Informe o valor da segunda nota: "))
valor3 = float(input("Informe o valor da terceira nota: "))
valor4 = float(input("Informe o valor da quarta nota: "))
peso_nota_1 = 1
peso_nota_2 = 3
peso_nota_3 = 2
peso_nota_4 = 4

media = (valor1*peso_nota_1 + valor2*peso_nota_2 + valor3*peso_nota_3 + valor4*peso_nota_4) / (peso_nota_1+peso_nota_2+peso_nota_3+peso_nota_4)

print("Media:", media)
"""
# 16 - Crie um programa que solicite o ângulo em graus e apresente o seno, cosseno e tangente deste ângulo.
"""angulo = float(input("Informe o ângulo em graus: "))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))

print("O seno de {} é {} , cosseno {}, Tangente {}.".format(angulo, seno, cosseno, tangente))
"""
# 17 - Antes de o racionamento de energia ser decretado, quase ninguém falava em quilowatts; mas, agora, todos incorporaram essa palavra em seu vocabulário. Sabendo-se que 100 quilowatts de energia custa um sétimo do salário mínimo, fazer um algoritmo que receba o valor do salário mínimo e a quantidade de quilowatts gasta por uma residência, calcule e imprima o valor em reais de cada quilowatt, o valor em reais a ser pago e o novo valor a ser pago por essa residência com um desconto de 10%.
"""salario = float(input("Informe o valor do salario minimo: "))
quilowatts = float(input("Informe o valor do quilowatts gasto: "))

cada_quilowatts = (salario/7)/100
valor_pago_real = quilowatts * cada_quilowatts
desconto = valor_pago_real * (10/100)
novo_valor = valor_pago_real - desconto

print("Novo valor a ser pago: ", novo_valor)"""

# 18 - Crie um algoritmo que, dado um nome, apresente ao usuário:
    #- o nome completo
    #- a primeira letra do nome
    #- a última letra do nome
    #- os caracteres do primeiro até o terceiro
    #- o quarto caractere
    #- todos os caracteres, menos o primeiro
    #- os dois últimos caracteres
"""
nome = "joao"

nome_completo = nome
primeira_letra = nome[0]
ultima_letra = nome[-3]
primeira_terceiro = nome[0, 2]

print("Nome completo", nome, "Primeira Letra nome:", primeira_letra, ultima_letra)
"""
#19 - Tendo-se os valores de a, b e c, calcule e exiba ao usuário o valor de x, conforme fórmula: x = a+ba+c+2a-b+log2 64 3*+1

"""a = int(input("Informe o primeiro valor: "))
b = int(input("Informe o segundo valor: "))
c = int(input("Informe o terceiro valor: "))

x = (a + (b/(a+c))+(2*(a-b))+math.log2*64) / 3*3.14 +1

print(x)"""

#20 - Efetuar o cálculo da quantidade de litros de combustível gastos em uma viagem, sabendo-se que o carro faz 12 km com um litro. Deverão ser fornecidos o tempo gasto na viagem e a velocidade média. O algoritmo deverá apresentar os valores da velocidade média, tempo gasto na viagem, distância percorrida e a quantidade de litros utilizados na viagem.
    #Fórmulas: distancia = tempo*velocidade      e    litrosUsados = distancia12
"""km_por_litro = 12

tempo_gasto = float(input("Informe o tempo gasto na viagem(em Horas): "))
velocidade_media = float(input("Informe a velocidade média(em km/H): "))

distancia = tempo_gasto * velocidade_media
litros_usado = distancia/12

print("A sua velocidade média foi {}Km/H, tempo gasto na viagem {} horas, distancia viajada {}Km e a quantidade de litros gastos foi de {} litros".format(velocidade_media, tempo_gasto, distancia, litros_usado))
"""
#21 - Uma calculadora pode ser feita via programação. Considere um algoritmo que faça a leitura de 2 números e de um operador matemático(‘+’, ‘-‘, ‘*’ ou ‘/’). O algoritmo deve efetuar o cálculo indicado no operador com os dois números informados e apresentar o resultado da operação. Exemplo: x = 10, y = 20, sinal = ‘+’. O resultado da operação deverá ser z = 30.

n1 = int(input("Informe um número inteiro: "))
n2 = int(input("Informe um segundo número inteiro: "))

print("('+' ,  '-',  '*'  ou  '/' )")
sinal = input("Escolha um operador matemático: ")

if(n1 >= 0 and n2 >=0 ):
    if(sinal == "+"):
        resultado = n1 + n2
        print("O resultado da soma é {} ".format(resultado))
    elif(sinal == "-"):
        resultado = n1 - n2
        print("O resultado da subtração é {} ".format(resultado))
    elif(sinal == "*"):
        resultado = n1 * n2
        print("O resultado da multiplicação é {} ".format(resultado))
    elif(sinal == "/"):
        resultado = n1 / n2
        print("O resultado da divisão é {} ".format(resultado))
    else:
        print("Operador matemático invalido")
else:
    print("Informe números validos.")

#22 - Tendo-se uma variável nome = “Dino da Silva Sauro”, como podemos apresentar na tela o tamanho desta String? (quantos caracteres tem).
"""nome = "Dino da Silva Sauro"
quantidade = len(nome)
print(quantidade)"""

#23 - Faça um algoritmo capaz de ler três números e exibir na tela se estes três valores podem ser lados de um triângulo. DICA: para saber se os três valores podem ser lados de um triângulo, cada valor deve ser menor que a soma dos dois outros valores.

"""n1 = float(input("Informe o primeiro numero:"))
n2 = float(input("Informe o segundo numero:"))
n3 = float(input("Informe o terceiro numero:"))

if(n1 < (n2 + n3) and n2 < (n1 + n3) and n3 < (n1 + n2)):
    print("Formam um triangulo")
else:
    print("Não formam um triangulo")"""

#25 - Um sistema informatizado precisa solicitar o estado de nascimento de uma pessoa. Baseado no estado informado, o sistema deve emitir uma das seguintes mensagens:

"""estado = input("Informe o seu estado de nascimento: ")

estado = str(estado).title()
print(estado)


if(estado == "Rio De Janeiro"):
    print("Carioca")
elif(estado == "São Paulo"):
    print("Paulistano")
elif(estado == "Minas Gerais"):
    print("Mineiro")
elif(estado == "Paraná"):
    print("Paranaense")
else:
    print("Outro estado do Brasil")"""

#26 - Crie um algoritmo que solicite a sigla do estado do usuário do sistema e apresente a respectiva mensagem conforme apresentado acima. O usuário poderá digitar tanto letras maiúsculas como minúsculas. Seu sistema deve tratar disto e exibir a mensagem correta.

"""sigla = input("Informe a sigla do seu estado de nascimento: ")

sigla = str(sigla).upper()
print("Sigla digitada", sigla)

if(sigla == "RJ"):
    print("Carioca")
elif(sigla == "SP"):
    print("Paulistano")
elif(sigla == "MG"):
    print("Mineiro")
elif(sigla == "PR"):
    print("Paranaense")
else:
    print("Outro estado do Brasil")"""

#27 - Crie um algoritmo que solicite por três valores inteiros. Em seguida, apresente se os três valores podem formar lados de um triângulo equilátero, escaleno ou isósceles, ou então não formar lados de um triângulo.

"""n1 = float(input("Informe o primeiro numero:"))
n2 = float(input("Informe o segundo numero:"))
n3 = float(input("Informe o terceiro numero:"))

if(n1 < (n2 + n3) and n2 < (n1 + n3) and n3 < (n1 + n2)):
    print("Formam um triangulo")

    if(n1 == n2 and n2 == n3):
        print("equilátero")
    else:
        if(n1 == n2 or n2 == n3 or n1 == n3):
            print("isósceles")
        else:
            print("escaleno")
else:
    print("Não formam um triangulo")

"""
#28 - Um sistema informatizado para a disciplina de Português precisa ser desenvolvido. Este sistema deve solicitar uma palavra ao usuário e informar se a palavra informada é um verbo ou não. Caso seja um verbo, o sistema deve informar se ele está na primeira conjugação (verbos terminados em ar), segunda conjugação (verbos terminados em er ou or) ou terceira conjugação (verbos terminados em ir).

"""
pessoas = ['Eu', 'Tu', 'Ele', 'Nós', 'Vós', 'Eles']
conjuga_ar = ['o', 'as', 'a', 'amos', 'ais', 'am']
conjuga_er = ['o', 'es', 'e', 'emos', 'eis', 'em']
conjuga_ir = ['o', 'es', 'e', 'imos', 'is', 'em']

verbo = str(input("Digite um verbo:"))
termina_em = verbo[-2:] 

if(termina_em) == "ar":
    print("primeira conjugação")
elif(termina_em) == "er":
    print("segunda conjugação")
elif(termina_em) == "ir":
    print("terceira conjugação")
else:
    print("Tem certeza que {} é um verbo?".format(verbo))
"""
#29 - Na disciplina de Algoritmos e Estruturas de Dados I, por ter muitos alunos, os professores decidiram que a turma seria dividida em dois laboratórios de informática para a realização das avaliações práticas. Esta divisão será dividida em três grupos baseando-se no nome de cada aluno.
    #Nome de aluno que inicie com as letras de A a K fará provas no Laboratório 1.
    #Nome de aluno que inicie com as letras de L a N fará provas no Laboratório 2.
    #Nome de aluno que inicie com as letras de O a Z fará provas no Laboratório 3.

"""a_k = ["A", "B", "C","D","E","F","G","H","I","J","K"]
l_m = ["L", "M", "N"]

nome_aluno = input("Informe o seu nome: ")

letra = nome_aluno[0]
letra = str(letra).upper()

if(letra in a_k):
    print("fará prova no Laboratório 1")

elif(letra in l_m):
    print("fará prova no Laboratório 2")

else:
    print("fará prova no Laboratório 3")
"""
#30 - Um sistema de atendimento da Empresa X precisa de um programa para atender o seguinte fluxo de navegação.
    #1 - Setor financeiro
    #1 - Consultar fatura atual
    #2 - Pagar fatura atual
    #3 - Parcelar fatura atual

    #2 - Alteração de plano
    #1 - Plano básico
    #2 - Plano intermediário
    #3 - Plano Combo Max Turbo

    #3 - Falar com atendente
    #4 - Sair
"""opcao = 0
while(opcao != 4):
    print("1 - Setor financeiro")
    print("2 - Alteração de plano")
    print("3 - Falar com atendente")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção: "))
    print(" ")
    if(opcao == 1):
        print("Escolheu opção {} Setor Financeiro.".format(opcao))
        print("\n  1 - Consultar fatura atual \n  2 - Pagar fatura atual \n  3 - Parcelar fatura atual")
        escolha = int(input("Escolha uma opção: "))
        if(escolha == 1):
            print("Escolheu opção {} consultar fatura atual.".format(opcao))
        elif(escolha == 2):
            print("Escolheu opção {} pagar fatura atual.".format(opcao))
        elif(escolha == 3): 
            print("Escolheu opção {} parcelar fatura atual".format(opcao))
        else:
            print("Opção invalida.")
        print(" ")
    elif(opcao == 2):
        print("Escolheu Alteração de plano")
        print("\n  1 - Plano básico \n  2 - Plano intermediário \n  3 - Plano Combo Max Turbo")
        escolha = int(input("Escolha uma opção: "))
        if(escolha == 1):
            print("Escolheu opção {} plano básico.".format(opcao))
        elif(escolha == 2):
            print("Escolheu opção {} plano intermediário.".format(opcao))
        elif(escolha == 3):
            print("Escolheu opção {} combo max turbo.".format(opcao))
        else:
            print("Opção invalida.")
        print(" ")
    elif(opcao == 3):
        print("Escolheu falar com atendente")
    elif(opcao == 4):
        print("Escolheu sair do sistema")
    else:
        print("Escolha uma oção valida")
    print("Esolha uma nova opção do sistema \n")

print("ATÉ MAIS..")"""

# Frequentemente os sistemas computacionais precisam lidar com datas, tais como data de cadastro, data de uma compra realizada, data de nascimento de um cliente, entre outras datas. As datas são formadas por dia, mês e ano. Implemente um algoritmo que faça a leitura de um dia, do mês e do ano e apresente uma mensagem na tela informando se a data é válida ou não. DICA: verificar se o mês está entre 1 e 12 e verificar se o dia é um número válido para àquele mês (verificar se o ano é bissexto).


#Um algoritmo deve ser desenvolvido, de forma que o usuário informe o nome de uma pessoa, a idade desta pessoa e o sexo desta pessoa (considere true para masculino e false para feminino). O sistema deve informar se a pessoa pode ser aceita em um determinado grupo ou não. Para que a pessoa possa ser aceita no grupo, considere:
    #• Mulher com mais de 30 anos
    #• Homem com mais de 25 anos
    #• Homens ou mulheres com idades entre 10 e 15 anos
    #Para todos os outros casos, a pessoa não será aceita no grupo.

"""nome = input("Informe o nome de uma pessoa: ")
idade = int(input("Informe a idade desta pessoa: "))
sexo = input("Informe o sexo desta pessoa('M' para Masculino ou 'F' para o sexo Femenino):")
sexo = sexo.upper()

if(sexo == "M" and idade >= 25):
    print("{} você pode ser aceito no grupo por ter {} anos".format(nome, idade))
elif(sexo == "F" and idade >= 30):
    print("{} você pode ser aceita no grupo por ter {} anos".format(nome, idade))
elif(sexo == "F" or sexo == "M" and idade >= 10 and idade <= 15):
    print("{} você pode ser aceita no grupo por ter {} anos é ser do sexo {}.".format(nome, idade))
else:
    print("Não pode ser aceito")"""



  
