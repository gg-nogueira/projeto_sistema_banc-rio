CREATE TABLE usuarios (
    cpf VARCHAR(11) PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    data_nascimento DATE NOT NULL,
    senha VARCHAR(6) NOT NULL,
    CONSTRAINT cpf_unique UNIQUE (cpf)
);

CREATE TABLE contas (
    numero_conta SERIAL PRIMARY KEY,
    cpf_usuario VARCHAR(11),
    saldo DECIMAL(10,2),
    CONSTRAINT contas_ibfk_1 FOREIGN KEY (cpf_usuario) REFERENCES usuarios (cpf)
);

CREATE TABLE historico (
    id SERIAL PRIMARY KEY,
    numero_conta INT,
    tipo_transacao VARCHAR(10) CHECK (tipo_transacao IN ('Depósito', 'Saque')),
    valor DECIMAL(10,2),
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT historico_ibfk_1 FOREIGN KEY (numero_conta) REFERENCES contas (numero_conta)
);
