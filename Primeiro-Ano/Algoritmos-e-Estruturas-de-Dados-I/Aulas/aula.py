import mysql.connector

# Criação de uma classe (registro)
class Disciplina:
    # Inicializando a classe
    def __init__(self):
        # Criação de atributos
        self.codigo = 0
        self.nome = ""
        self.ch = 0
        self.professor = ""
        self.chr = 0.0

def salvar(d):
    banco = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "banco_teste"
    )

    cursor = banco.cursor()
    
    sql = "INSERT INTO disciplina VALUES (%s, %s, %s, %s, %s);"
    valores = (None, d.nome, d.ch, d.professor, d.chr)

    cursor.execute(sql, valores)
    banco.commit()

    # busca o valor do ID gerado e coloca
    # no objeto "d"
    d.codigo = cursor.lastrowid

    cursor.close()
    banco.close()

    # Fim da função


def lerDados():
    banco = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="algoritmos"
    )

    cursor = banco.cursor()

    sql = "SELECT * from disciplina ORDER BY nome"

    cursor.execute(sql)

    # Converte os dados obtidos no select na tabela
    # para um vetor e guarda na variável
    dados = cursor.fetchall()

    # Criar um vetor para armazenar as disciplinas em forma de objetos
    vetor = [Disciplina()] * cursor.rowcount
    
    # para controlar o índice do vetor "x"
    i = 0
    
    # Criar uma disciplina PARA cada registro do banco
    for tupla in dados:
        
        # Cria um objeto do tipo Disciplina
        obj = Disciplina()
        
        # As posições da linha são as ordens dos dados nas colunas
        obj.codigo = tupla[0]
        obj.nome = tupla[1]        
        obj.ch = tupla[2]
        obj.professor = tupla[3]
        obj.chr = tupla[4]

        # Guarda esse objeto no vetor
        vetor[i] = obj

        # Aumenta o valor de i para a próxima posição
        i += 1

    return vetor

# Pede para o usuário digitar os dados e retorna o objeto
def pedirDisc():
    disc = Disciplina()
    disc.nome = input("Nome: ")
    disc.ch = int(input("CH: "))
    disc.professor = input("Professor: ")
    disc.chr = (disc.ch * 50) / 60
    
    return disc

# Digitar dados
disciplina = pedirDisc()

# Salva esse objeto no banco
salvar(disciplina)

# Chama a função para trazer os dados do banco
x = lerDados()

print("\n\n---- Disciplinas cadastradas ----")

# Percorre o vetor de disciplinas
for i in range(0, len(x)):
    
    # Cria uma variável pra receber o objeto
    disc = x[i] 

    print("Código:", disc.codigo)
    print("Nome:", disc.nome)
    print("CH:", disc.ch)
    print("Professor:", disc.professor)
    print("CHR:", disc.chr)

    print("")

