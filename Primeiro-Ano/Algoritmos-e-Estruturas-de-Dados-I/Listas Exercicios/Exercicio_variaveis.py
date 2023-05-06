idade = int(input("Informe sua idade: "))

nome = input("Informe seu Nome: ")

sobrenome = input("Informe seu Sobrenome: ")

nome_completo = nome + " " + sobrenome

altura = float(input("Informe sua Altura: "))

peso = float(input("Informe seu Peso: "))

estudos = int(input("Informe quantos dias na semana você estuda Algoritimos: "))

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
