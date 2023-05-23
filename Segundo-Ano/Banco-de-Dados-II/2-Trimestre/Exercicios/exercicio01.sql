DROP TABLE IF EXISTS ser;
DROP TABLE IF EXISTS arma;
DROP TABLE IF EXISTS local;
DROP TABLE IF EXISTS raca;
DROP TABLE IF EXISTS classe;

CREATE TABLE classe(
	id_classe SERIAL PRIMARY KEY,
	nome VARCHAR(255),
	proficiencia VARCHAR(255) 
);

CREATE TABLE arma(
	id_arma SERIAL PRIMARY KEY,
	nome VARCHAR(255),
	tipo VARCHAR(255),
	magica BOOLEAN,
	lendaria BOOLEAN
);

CREATE TABLE raca(
	id_raca SERIAL PRIMARY KEY,
	nome VARCHAR(255),
	altura_media DECIMAL(10,0)
);

CREATE TABLE local(
	id_local SERIAL PRIMARY KEY,
	nome VARCHAR(255),
	regiao VARCHAR(255),
	raca_id INTEGER REFERENCES raca(id_raca)
);

CREATE TABLE ser(
	id_ser SERIAL PRIMARY KEY,
	nome VARCHAR(255),
	titulo VARCHAR(255),
	familia VARCHAR(255),
	nascimento DATE,
	raca_id INTEGER REFERENCES raca(id_raca),
	local_id INTEGER REFERENCES local(id_local),
	classe_id INTEGER REFERENCES classe(id_classe),
	arma_id INTEGER REFERENCES arma(id_arma)
);

/* INSERT FEITOS PELO CHATGPT*/
INSERT INTO classe (nome, proficiencia)
VALUES ('Guerreiro', 'Armas de combate corpo a corpo'),
	   ('Mago', 'Magias e feitiços elementais'),
	   ('Arqueiro', 'Armas de longo alcance'),
	   ('Ladrão', 'Habilidades furtivas e arrombamento'),
	   ('Bardo', NULL),
	   ('Paladino', NULL);
	   
		
INSERT INTO arma (nome, tipo, magica, lendaria) 
VALUES ('Espada Longa', 'Espada', FALSE, FALSE),
	   ('Cajado do Fogo', 'Cajado', TRUE, FALSE),
	   ('Arco Élfico', 'Arco', FALSE, FALSE),
	   ('Adaga Envenenada', 'Adaga', FALSE, FALSE),
	   ('Machado de Batalha', 'Machado', NULL, FALSE),
	   ('Cajado das Sombras', 'Cajado', TRUE, FALSE);


INSERT INTO raca (nome, altura_media)
VALUES ('Humano', 180),
	   ('Elfo', 170),
	   ('Anão', 150),
	   ('Orc', 190),
	   ('Goblin', NULL),
	   ('Vampiro', NULL);

INSERT INTO local (nome, regiao, raca_id)
VALUES ('Cidade Real', 'Reino do Sul', 1),
	    ('Floresta Élfica', 'Reino Élfico', 2),
	    ('Montanhas de Ferro', 'Reino Anão', 3),
	    ('Terras Selvagens', 'Reino dos Orcs', 4),
	    ('Cidade do Caos', NULL, 3),
	    ('Terras Desconhecidas', 'Desconhecido', NULL);

INSERT INTO ser (nome, titulo, familia, nascimento, raca_id, local_id, classe_id, arma_id)
VALUES ('Aragorn', 'O Herdeiro de Gondor', 'Dúnedain', '1990-03-15', 1, 1, 1, 1),
	   ('Gandalf', 'O Mago Cinzento', 'Istari', '1500-10-31', 2, 2, 2, 2),
	   ('Legolas', 'O Arqueiro Élfico', 'Reino Élfico', '1985-06-24', 2, 2, 3, 3),
	   ('Grommash', 'O Devorador', 'Clã Rocha Negra', '1973-09-07', 4, 4, 4, 4),
	   ('Frodo Bolseiro', 'Portador do Anel', NULL, '1980-09-22', NULL, 2, NULL, 1),
	   ('Sauron', NULL, NULL, '1500-01-01', 4, NULL, 1, NULL);

-- A
SELECT a.nome, l.nome
FROM arma a
LEFT JOIN ser s ON s.arma_id = a.id_arma
LEFT JOIN local l ON s.local_id = l.id_local
WHERE s.arma_id IS NOT NULL AND s.local_id IS NOT NULL
GROUP BY a.nome, l.nome;

-- B
/* SELECT c.nome, l.regiao
FROM classe c
LEFT JOIN ser s ON s.classe_id = c.id_classe
LEFT JOIN local l ON s.local_id = l.id_local
GROUP BY c.nome, l.regiao; */
		
SELECT c.nome AS classe, l.regiao
FROM classe c
CROSS JOIN local l;

-- C
SELECT a.tipo, r.nome
FROM arma a
FULL JOIN ser s ON s.arma_id = a.id_arma
LEFT JOIN raca r ON s.raca_id = r.id_raca
WHERE s.arma_id IS NOT NULL AND s.raca_id IS NOT NULL
GROUP BY a.tipo, r.nome;

