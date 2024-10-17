CREATE DATABASE BancoGAN;
USE BancoGAn;

CREATE TABLE usuarios (
	cpf VARCHAR(11) NOT NULL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    data_nascimento DATE NOT NULL,
    senha VARCHAR(6) NOT NULL
);
    
CREATE TABLE contas (
	numero_conta INTEGER PRIMARY KEY auto_increment,
    saldo DECIMAL (10,2) DEFAULT 0,
    cpf_user VARCHAR(11),
    FOREIGN KEY (cpf_user) REFERENCES usuarios(cpf)
);
    
    CREATE TABLE historico_transacoes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    numero_conta INT,
    tipo_transacao ENUM('Depósito', 'Saque'),
    valor DECIMAL(10, 2),
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (numero_conta) REFERENCES contas(numero_conta)
);