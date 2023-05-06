"""import mysql.connector

class Cargo:
    def __init__(self):
        self.descricao = ""
        self.salarioAdicional = 0.0

class Profissao:
    def __init__(self):
        self.descricao = ""
        self.registro = False

class Funcionario:
    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.salario = 2000.0
        self.cargo = Cargo()
        self.profissao = Profissao()


def salvarDados(d):
    banco = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "algoritimos"

    )

    cursor = banco.cursor()

    sql_funcionario = "INSERT INTO funcionario VALUES (%s,%s,%s,%s,%s)"
    valores_funcionario = (None, d.nome, d.idade, d.salario, d.cargo, d.profissao)

    sql_cargo = "INSERTO INTO cargo VALUES (%s,%s,%s)"
    valores_cargo = (None, d.descricao, d.salarioAdicional)

    sql_profissao = "INSERT INTO profissao VALUES (%s,%s,%s)"
    valores_profissao = (None, d.descricao, d.salarioAdicional)

    
    cursor.execute(sql_funcionario, valores_funcionario)
    cursor.execute(sql_cargo, valores_cargo)
    cursor.execute(sql_profissao, valores_profissao)
    banco.commit()

    d.codigo = cursor.lastrowid()

    cursor.close()
    banco.close()




def lerDados():
    banco = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "algoritimos"
    )

    cursor = banco.cursor()

    sql = "SELECT * FROM funcionario ORDER BY nome"

    cursor.execute(sql)

    dados = cursor.fetchall()

    vetor = [Funcionario()] * cursor.rowcount

    for linha in dados:

        obj = Funcionario()

        obj.nome = linha[0]
        obj.idade = linha[1]
        obj.salario = linha[2]
        obj.cargo = linha[3]
        obj.profissao = linha[4]

        vetor[linha] = obj
    
    return vetor

def infoFuncionario():

    fun = Funcionario()
    fun.nome = input("Informe o nome do Funcionario: ")
    fun.idade = int(input("Idade: "))

    #Cargo
    fun.cargo.descricao = input("Informe seu cargo: ")
    fun.cargo.salarioAdicional = float(input("Informe o adicional de salario: "))

    fun.salario += (fun.cargo.salarioAdicional)

    fun.profissao.descricao = input("Informe a descrição da Profissão: ")

    return fun


funcionario = infoFuncionario()
salvarDados(funcionario)
x = lerDados()"""
"""
a = int(input("valor: "))
b = int(input("valor: "))
c = int(input("valor: "))

triangulo = a * c/2
circulo = (3.14159 * (c**2))
trapezio = (a+b)*c/2
quadrado = b*b
retangulo = a*b

print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")"""
"""
import math

a = int(input("v:"))
b = int(input("v:"))
c = int(input("v:"))

maior = (a + b + abs(a-b))/2
resultado = (maior + c + abs(maior-c))/2

print(f"{resultado:.0f} eh o maior")"""

tempo_gasto = float(input())
velocidade_media = float(input())

distancia_percorrida = tempo_gasto * velocidade_media
litros_combustivel = distancia_percorrida / 12

print("{:.3f} ".format(litros_combustivel))





