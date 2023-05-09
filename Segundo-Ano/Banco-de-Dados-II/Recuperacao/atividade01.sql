DROP DATABASE IF EXISTS teste_aula;
CREATE DATABASE teste_aula;
USE teste_aula;

CREATE TABLE estado(
	id_estado SERIAL PRIMARY KEY,
	nome_estado VARCHAR(100) NOT NULL,
	sigla char(2) NOT NULL
);

CREATE TABLE cidade(
	id_cidade SERIAL PRIMARY KEY,
	nome_cidade VARCHAR(255) NOT NULL,
	estado_id INTEGER REFERENCES estado(id_estado)
);

CREATE TABLE funcionario(
	id_funcionario SERIAL PRIMARY KEY,
	nome_funcionario VARCHAR(255) NOT NULL,
	funcao VARCHAR(255) NOT NULL,
	cidade_id INTEGER REFERENCES cidade(id_cidade)
);

CREATE TABLE cliente(
	id_cliente SERIAL PRIMARY KEY,
	nome_cliente VARCHAR(255) NOT NULL,
	cpf_cliente VARCHAR(20) NOT NULL,
	cidade_id INTEGER REFERENCES cidade(id_cidade)
);

CREATE TABLE categoria(
	id_categoria SERIAL PRIMARY KEY,
	nome_categoria VARCHAR(255) NOT NULL
);

CREATE TABLE produto(
	id_produto SERIAL PRIMARY KEY,
	nome_produto VARCHAR(255) NOT NULL,
	valor_unitario DECIMAL(5,2) NOT NULL,
	categoria_id INTEGER REFERENCES categoria(id_categoria)
);

CREATE TABLE venda(
	id_venda SERIAL PRIMARY KEY,
	funcionario_id INTEGER REFERENCES funcionario(id_funcionario),
	cliente_id INTEGER REFERENCES cliente(id_cliente),
	produto_id INTEGER REFERENCES produto(id_produto),
	quantidade_produto INT NOT NULL,
	valor_total DECIMAL(5,2) NOT NULL,
	data_venda DATE NOT NULL
);

INSERT INTO estado(nome_estado, sigla)
VALUES ('Parana', 'PR'),
	   ('São Paulo', 'SP'),
	   ('Rio de Janeiro', 'RJ');
	   
INSERT INTO cidade(nome_cidade, estado_id)
VALUES ('Paranavaí', 1),
	   ('Rio de Janeiro', 3),
	   ('São Paulo', 2);

INSERT INTO funcionario(nome_funcionario, funcao, cidade_id)
VALUES ('João', 'Dono', 1),
	   ('Back', 'Gerente', 3),
	   ('Luiz', 'Assistente', 2);
       
INSERT INTO cliente(nome_cliente, cpf_cliente, cidade_id)
VALUES ('Matheus', '12345678910', 2),
	   ('Liu', '12345678910', 1),
       ('Arthur', '12345678910', 1);

INSERT INTO categoria(nome_categoria)
VALUES ('PC'),
	   ('Mobile'),
	   ('Console');

INSERT INTO produto(nome_produto, valor_unitario, categoria_id)
VALUES ('Red Dead 2', 150.00, 1),
	   ('Cyberpunk', 255.00, 3),
	   ('Free Fire', 500.00, 2);
	   
INSERT INTO venda(funcionario_id, cliente_id, produto_id, quantidade_produto, valor_total, data_venda)
VALUES (1, 2, 1, 2, 300.00, '2022-01-11'),
	   (2, 2, 1, 2, 300.00, '2022-01-30'),
       (3, 2, 1, 2, 300.00, '2022-02-20'),
	   (1, 3, 2, 1, 200.00, '2022-05-11'),
	   (3, 1, 3, 4, 600.00, '2023-06-11'),
       (1, 1, 3, 4, 600.00, '2023-07-11');

SELECT fun.nome_funcionario, c.nome_cidade, COUNT(v.data_venda) AS quantidade_de_vendas
FROM funcionario fun
INNER JOIN cidade c ON c.id_cidade = fun.cidade_id
INNER JOIN venda v ON v.funcionario_id = fun.id_funcionario
WHERE v.data_venda >= '2022-01-01' AND v.data_venda <= '2023-01-011'
GROUP BY fun.nome_funcionario, c.nome_cidade
ORDER BY quantidade_de_vendas DESC;