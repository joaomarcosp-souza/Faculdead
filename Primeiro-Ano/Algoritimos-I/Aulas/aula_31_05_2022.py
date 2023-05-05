import random
import math

"""n1 = int(input("informe o primeiro valor: "))
n2 = int(input("Informe o valor maior que o primeiro: "))

rd = random.randint(n1,n2)
rd2d = random.randint(n1,n2)

if(rd > rd2d):
    print("o {}  é maior que {}".format(rd, rd2d))
elif(rd == rd2d):
    print("Valores iguais")
else:
    print("o {} é maior que {}".format(rd2d, rd))
"""

n1 = float(input("Digite um numero: "))
r = math.sqrt(n1) #raiz quadrada
p = math.pow(n1,3) # potencia de expontes
f = math.floor(8.96) #arrendo pra baixo
c = math.ceil(8.102) #arrendo pra cima

print("A raiz de {} é, {}".format(n1, r))
print("{} elevado a 3 é {}".format(n1, p))
print("Piso de 8.96 é {}".format(f))
print("Teto de 8.102 é {}".format(c))