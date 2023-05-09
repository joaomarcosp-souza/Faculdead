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
VALUES ('Pão'),
	   ('Assado'),
	   ('Esfirra');

INSERT INTO produto(nome_produto, valor_unitario, categoria_id)
VALUES ('Pão', 1.50, 1),
	   ('Pão Frances', 2.50, 1),
       ('Pizza', 2.50, 3),
	   ('Baguetinho ', 3.00, 1);
	   
INSERT INTO venda(funcionario_id, cliente_id, produto_id, quantidade_produto, valor_total, data_venda)
VALUES (1, 2, 1, 8, 10.00, '2022-01-11'),
	   (2, 3, 3, 10, 20.00, '2023-02-11'),
	   (3, 1, 2, 25, 30.00, '2023-06-11');
       
SELECT c.nome_cliente, e.sigla, p.nome_produto, v.valor_total
FROM venda v
INNER JOIN cliente c ON c.id_cliente = v.cliente_id
INNER JOIN cidade cid ON cid.id_cidade = c.cidade_id
INNER JOIN estado e ON e.id_estado = cid.estado_id
INNER JOIN produto p ON p.id_produto = v.produto_id
WHERE p.nome_produto LIKE 'Pão%'
GROUP BY c.nome_cliente
ORDER BY v.valor_total