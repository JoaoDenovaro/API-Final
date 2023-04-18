CREATE DATABASE locacao_api;

USE locacao_api;

CREATE TABLE locadora (
    uuid CHAR(36) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    horario_abertura TIME NOT NULL,
    horario_fechamento TIME NOT NULL,
    endereco VARCHAR(255) NOT NULL
);

CREATE TABLE pessoa (
    uuid CHAR(36) PRIMARY KEY,
    cnh CHAR(11) UNIQUE NOT NULL,
    tipo VARCHAR(30) NOT NULL,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE veiculo (
    uuid CHAR(36) PRIMARY KEY,
    uuid_condutor CHAR(36) NOT NULL,
    placa CHAR(7) UNIQUE NOT NULL,
    modelo VARCHAR(30) NOT NULL,
    tipo VARCHAR(30) NOT NULL,
    combustivel VARCHAR(30) NOT NULL,
    capacidade TINYINT NOT NULL,
    cor VARCHAR(30) NOT NULL,
    FOREIGN KEY (uuid_condutor)
    REFERENCES pessoa(uuid)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT
);

CREATE TABLE usuario (
    uuid CHAR(36) PRIMARY KEY,
    uuid_pessoa CHAR(36) UNIQUE NOT NULL,
    acesso VARCHAR(20) UNIQUE NOT NULL,
    salt_senha BINARY(29) NOT NULL,
    hash_senha BINARY(60) NOT NULL, 
    FOREIGN KEY (uuid_pessoa)
    REFERENCES pessoa(uuid)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT
);

INSERT INTO TABLE pessoa 
VALUES ('8d0cd491-9ac8-467d-8631-617f5f65bd0e', '82027447451', 'Colaborador', 'João')