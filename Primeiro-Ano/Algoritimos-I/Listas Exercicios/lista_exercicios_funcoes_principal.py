import lista_exercicios_funcoes

#1
num = lista_exercicios_funcoes.NumeroInteiro()
print("Número inteiro informado: {}".format(num))

#2
numAle = lista_exercicios_funcoes.NumeroAleatorio(num)
print("Número Aléatorio gerado: {}".format(numAle))

#3
numMes = lista_exercicios_funcoes.RetornaMes(numAle)
print("Mês Correspondente: {}".format(numMes))

#4

"""#5
numFat = lista_exercicios_funcoes.fatorial(num)
print("O fatorial {}".format(numFat))

#6
fatNRep = lista_exercicios_funcoes.fatNoRepeat(num)
print("O fatorial {}".format(fatNRep))
"""
#7 #8
vetor = [89,54,74,43,75,200]
maior = lista_exercicios_funcoes.maior(vetor)
menor = lista_exercicios_funcoes.menorValor(vetor)
print("O Maior número dentro do vetor {} é o menor {}".format(maior, menor))

#9
media = lista_exercicios_funcoes.media(vetor)
print("A media é {}".format(media))

#10
vetor2 = [89,54,74,43,75,200,23,24,51,56,76,21]
dobro = lista_exercicios_funcoes.calDobro(vetor2)
print("O dobro dos números é {}".format(dobro))

#11
data = "25/10/2022"
