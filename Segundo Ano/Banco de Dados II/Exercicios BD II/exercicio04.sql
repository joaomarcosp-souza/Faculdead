CREATE TABLE usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
	email VARCHAR(100) NOT NULL
);

CREATE TABLE pedidos (
    id_pedido SERIAL PRIMARY KEY,
	valor DECIMAL(10,2),
	data_pedido DATE NOT NULL,
    id_usuario INTEGER REFERENCES usuarios(id_usuario)
);

INSERT INTO usuarios (nome, email)
VALUES ('João', 'jao@gmail.com'),
	   ('Backe', 'backe@gmail.com'),
       ('Luis', 'luis@gmail.com'),
       ('Cauê', 'caue@gmail.com');

INSERT INTO pedidos (valor, data_pedido, id_usuario)
VALUES (25.00, '2023-02-03', 1),
       (53.10, '2022-01-02', 2),
       (100.00, '2022-01-20', 3),
       (63.50, '2023-01-02', 4);

SELECT u.nome, MIN(p.data_pedido) AS primeiro_pedido
FROM usuarios u
JOIN pedidos p ON p.id_usuario = u.id_usuario
GROUP BY u.nome
ORDER BY primeiro_pedido
LIMIT 1;
