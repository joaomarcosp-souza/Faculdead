import mysql.connector

from mysql.connector import errorcode


banco = mysql.connector.connect(
		host='localhost', user='root', password='', database='algoritmos')
print("Conexão estabelecida!")
    

#Executa uma consulta precisamos de um "ponteiro" para o banco
cursor = banco.cursor()

#Inserindo valores no banco
sql = "INSERT INTO disciplinas (nome, ch, professor) VALUES (%s,%s,%s)"
valor1 = ("Algoritmos", "160", "Rafael")
valor2 = ("Portugues", "250", "Ana Carolina")
valor3 = ("Engenharia de software", "500", "André")

#execulta consulta
cursor.execute(sql, valor1)
cursor.execute(sql, valor2)
cursor.execute(sql, valor3)

#salva a consulta feita no banco de dados
banco.commit()
#fecha o banco
banco.close()
