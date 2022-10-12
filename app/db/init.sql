USE carford_db;


CREATE TABLE proprietarios(
id int(4) AUTO_INCREMENT,
nome varchar(45) NOT NULL,
oportunidade_venda boolean NOT NULL,
PRIMARY KEY (id)
);

CREATE TABLE carros(
id int(4) AUTO_INCREMENT,
modelo varchar(45) NOT NULL,
cor varchar(45) NOT NULL,
proprietario_id int(4),
PRIMARY KEY (id)
);