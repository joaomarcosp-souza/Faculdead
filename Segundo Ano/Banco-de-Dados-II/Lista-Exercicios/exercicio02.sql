CREATE TABLE pedidos (
    id_pedido SERIAL PRIMARY KEY,
    data_pedido DATE NOT NULL,
	valor_total DECIMAL(5,2) NOT NULL
);

CREATE TABLE produtos (
    id_produto SERIAL PRIMARY KEY,
    nome_produto VARCHAR(150) NOT NULL,
	descricao VARCHAR(200) NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL
);

CREATE TABLE itens_pedido (
    id_item SERIAL PRIMARY KEY,
    quantidade INT NOT NULL,
    valor_unitario DECIMAL(10,2) NOT NULL,
    pedido_id INTEGER REFERENCES pedidos(id_pedido),
    produto_id INTEGER REFERENCES produtos(id_produto)
);

INSERT INTO pedidos (data_pedido, valor_total)
VALUES ('2023-02-01', 50),
       ('2023-04-02', 85),
       ('2023-02-03', 96);
	   
INSERT INTO produtos (nome_produto, descricao, preco_unitario)
VALUES ('Pepsi', '500ml', 5),
       ('Coca-Cola', '2 Litros', 15),
       ('X-Tudo', 'Vem Tudo', 30);
	 
INSERT INTO itens_pedido (pedido_id, produto_id, quantidade, valor_unitario)
VALUES (1, 1, 5, 10),
       (1, 2, 6, 20),
       (2, 1, 8, 10),
       (2, 3, 4, 30),
       (3, 2, 12, 20),
       (3, 3, 15, 30);

SELECT p.id_pedido, SUM(ip.quantidade) AS total_itens
FROM pedidos p
JOIN itens_pedido ip ON p.id_pedido = ip.pedido_id
GROUP BY p.id_pedido
HAVING SUM(ip.quantidade) > 10
ORDER BY p.id_pedido;
