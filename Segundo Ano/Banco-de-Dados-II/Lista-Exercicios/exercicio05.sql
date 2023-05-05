/*Dado o esquema abaixo, escreva uma consulta que retorne o nome do produto e a quantidade vendida 
nos últimos 30 dias:
Produto (id, nome, preço)
Venda (id, produto_id, quantidade, data)*/

CREATE TABLE produto(
	id_produto SERIAL PRIMARY KEY,
	nome_produto VARCHAR(100) NOT NULL,
	preco_produto DECIMAL(5,2) NOT NULL
);

CREATE TABLE venda(
	id_venda SERIAL PRIMARY KEY,
	produto_id INTEGER REFERENCES produto(id_produto),
	quantidade INT NOT NULL,
	data_venda DATE NOT NULL
);

INSERT INTO produto (nome_produto, preco_produto) 
VALUES ('Coca-cola', 10.00),
       ('Salgado', 100.00),
       ('Pizza', 50.00),
       ('Guarana', 10.00);
	   
INSERT INTO venda (produto_id, quantidade, data_venda)
VALUES (1, 10, '2022-01-12'),
	   (1, 10, '2023-01-08'),
	   (1, 10, '2023-02-01'),
	   (1, 10, '2023-03-25');

SELECT p.nome_produto, SUM(v.quantidade) AS quantidade_vendida
FROM produto p 
JOIN venda v ON v.produto_id = p.id_produto
WHERE v.data_venda >= CURRENT_DATE - INTERVAL '30 days' /*Pegando a data atual e subtraindo por 30*/
GROUP BY p.nome_produto;



