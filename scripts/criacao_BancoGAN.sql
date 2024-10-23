CREATE DATABASE BancoGAN;
USE BancoGAn;

CREATE TABLE usuarios (
    cpf VARCHAR(11) PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    data_nascimento DATE NOT NULL,
    senha VARCHAR(6) NOT NULL,
    CONSTRAINT cpf_unique UNIQUE (cpf)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

CREATE TABLE contas (
    numero_conta INT PRIMARY KEY AUTO_INCREMENT,
    cpf_usuario VARCHAR(11),
    saldo DECIMAL(10,2),
    CONSTRAINT contas_ibfk_1 FOREIGN KEY (cpf_usuario) REFERENCES usuarios (cpf)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

CREATE TABLE historico (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tipo_transacao ENUM('Depósito', 'Saque'),
    valor DECIMAL(10,2),
	data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT historico_ibfk_1 FOREIGN KEY (numero_conta) REFERENCES contas(numero_conta
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
