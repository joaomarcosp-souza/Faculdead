class Aluno:
    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.email = ""
        self.sexo = False #False: feminino


class Data:
    def __init__(self):
        self.dia = 0
        self.mes = 0
        self.ano = 0

b = Aluno()
b.nome = input("Informe seu nome: ")
b.idade = int(input("informe sua idade: "))
b.email = input("Informe seu e-mail: ")
b.sexo = True

print("Nome: {} \n idade {} \n email {}".format(b.nome, b.idade, b.email))


d = Data()
d.dia = int(input("Informe dia de hoje: "))
d.mes = int(input("Informe o mês: "))
d.ano = int(input("Informe o ano: "))

print("A data de hoje é: {}/{}/{}".format(d.dia, d.mes, d.ano))
