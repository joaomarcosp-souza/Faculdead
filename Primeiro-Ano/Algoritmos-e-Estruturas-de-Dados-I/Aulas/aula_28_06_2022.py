
""""import sys
maior = -sys.maxsize-1
menor = sys.maxsize"""

maior = -9999999999999
menor = 99999999999999
par = 0
impar = 0
for i in range(0,6):
    x = int(input("Informe um numero: "))
    if(x > maior):
        maior = x
    elif(x < menor):
        menor = x
    
    if(x % 2 == 0):
        par += 1
    else:
        impar += 1
    
print("o maior numero é: ",maior)
print("o menor numero é: ",menor)
print("impar {}, par {}".format(impar, par))



"""x = 0
while(x <= 100):
    if(x % 3 == 0):
        print(x)
    x += 1
"""