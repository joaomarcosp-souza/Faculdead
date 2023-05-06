
DROP DATABASE IF EXISTS aula_banco; -- eliminando aula_banco
CREATE DATABASE aula_banco;	 		-- criando aula_banco
USE aula_banco;	 					-- selecionando aula_banco

DROP TABLE IF EXISTS estado;

-- criando tabela ESTADO
CREATE TABLE estado(
id INT NOT NULL AUTO_INCREMENT,
nome VARCHAR(200) NOT NULL UNIQUE, 	-- constraint inline - regras na mesma linha
sigla CHAR(2) NOT NULL UNIQUE,
ativo CHAR(1) NOT NULL DEFAULT 'S',
data_cadastro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
CONSTRAINT pk_estado PRIMARY KEY(id),
CONSTRAINT coluna_ativo_deve_ser_S_ou_N CHECK (ativo IN('S', 'N')) -- constraint off line - regras definidas fora da linha de coluna
);

-- inserindo dados na tabela ESTADO
INSERT INTO estado (nome, sigla) VALUES ('PARANÁ', 'PR');
INSERT INTO estado (nome, sigla) VALUES ('GOIAS', 'GO');
INSERT INTO estado (nome, sigla) VALUES ('MATO GROSSO', 'MT');

-- inserindo dados na tabela ESTADO
SELECT id, nome, sigla, ativo, data_cadastro FROM estado;

/** 
VERIFICANDO A PADRONIZAÇÃO DO CÓDIGO
*/