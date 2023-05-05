CREATE TABLE cliente (
    id_cliente SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
	endereco VARCHAR(200) NOT NULL,
    cidade VARCHAR(100) NOT NULL, 
	estado VARCHAR(100) NOT NULL
);

CREATE TABLE pedidos (
    id_pedido SERIAL PRIMARY KEY,
	data_pedido DATE NOT NULL,
	valor_total DECIMAL(10,2),
    id_cliente INTEGER REFERENCES cliente(id_cliente)
);

INSERT INTO cliente (nome, endereco, cidade, estado)
VALUES ('João', 'Rua Não Sei', 'Paranavaí', 'Paraná'),
	   ('Backe', 'Rua Sei lá', 'Maringa', 'Paraná'),
       ('Luis', 'Rua Santos', 'Londrina', 'Paraná'),
       ('Cauê', 'Rua Verdinha', 'Curitiba', 'Paraná');

    
INSERT INTO pedidos (data_pedido, valor_total, id_cliente)
VALUES ('2023-02-03', 25.00, 1),
       ('2022-01-02', 53.10, 2),
       ('2022-01-20', 100.00, 3),
       ('2023-01-02', 63.50, 4);

SELECT c.nome, SUM(p.valor_total) AS valor_total
FROM cliente c
JOIN pedidos p ON p.id_cliente = c.id_cliente
WHERE p.data_pedido >= '2022-01-01' AND p.data_pedido <= '2022-02-01'
GROUP BY c.nome
ORDER BY valor_total DESC;

