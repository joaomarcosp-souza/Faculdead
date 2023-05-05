import random

"""Escrever um algoritmo que leia as 3 notas obtidas por um aluno(de 0 a 100), calcule e mostre na tela a média obtida pelo aluno. Em seguida, o algoritmo deve apresentar qual foi o conceito equivalente obtido por este aluno. Sabe-se que:

Conceito A: média de 90 a 100

Conceito B: média entre 75 e 89

Conceito C: média entre 55 e 74

Conceito D: média entre 0 e 54."""

nota01 = int(input("Informe a primeira nota obtida (de 0 a 100): "))
nota02 = int(input("Informe a segunda nota obtida (de 0 a 100): "))
nota03 = int(input("Informe a terceira nota obtida (de 0 a 100): "))

media = (nota01 + nota02 + nota03) / 3
if(media >= 0 and media <= 54):
    print("media obtida foi {} portanto ficou com conceito D".format(media))

elif(media >= 55 and media <= 74):
    print("media obtida foi {} portanto ficou com conceito C".format(media))

elif(media >= 75 and media <= 89):
    print("media obtida foi {} portanto ficou com conceito B".format(media))

else:
    print("media obtida foi {} portanto ficou com conceito A".format(media))


numero = int(input("Informe um numero entre(0 e 10): "))

if(numero >= 0 and numero <=10):
    escolha = input("Informe 'par' ou 'impar': ")

    numero_random = random.randint(0, 10)
    soma = numero + numero_random

    print("O numero random foi {} a soma do numero random mais o primeiro numero {} foi {} e você escolheu {} então: ".format(numero_random,numero, soma, escolha))

    soma = soma % 2 == 0

    if(escolha == "par" and soma):
        print("Ganhou o jogo")
    else:
        print("Perdeu o jogo")
else:
    print("O numero informado não está entre 0 e 10")
