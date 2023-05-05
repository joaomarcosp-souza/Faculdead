CREATE TABLE departamento (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL
);

CREATE TABLE funcionario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    idade INTEGER NOT NULL,
    salario INTEGER NOT NULL,
    departamento_id INTEGER REFERENCES departamento(id)
);

INSERT INTO departamento (id, nome)
VALUES (1, 'Financeiro'),
       (2, 'Vendas');

INSERT INTO funcionario (id, nome, idade, salario, departamento_id)
VALUES (1, 'João', 25, 3000, 1),
       (2, 'Maria', 30, 2500, 2),
       (3, 'José', 35, 2000, 1),
       (4, 'Ana', 28, 3200, 1),
       (5, 'Carlos', 27, 2800, 2),
       (6, 'Juliana', 33, 2900, 2),
       (7, 'Rafaela', 29, 2800, 1),
       (8, 'Fernanda', 24, 2700, 1),
       (9, 'Guilherme', 31, 2200, 2),
       (10,'Henrique',26 ,1000 ,2);

SELECT f.nome
FROM funcionario f
JOIN departamento ON f.departamento_id = departamento.id
WHERE f.salario BETWEEN 2000 AND 3000
ORDER BY departamento.nome DESC, f.nome
