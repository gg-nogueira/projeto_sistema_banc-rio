import re
import random
import mysql


# Expressões regulares para validação de CPF e senha
cpf_regex = re.compile(r'^\d{11}$')  # regex de CPF
senha_regex = re.compile(r'^\d{6}$')

def criar_usuario(conexao):
    cursor = conexao.cursor()

    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF (somente números): ")
    data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")

    # Verificar se o CPF já existe no banco de dados
    cursor.execute("SELECT cpf FROM usuarios WHERE cpf = %s", (cpf,))
    if cursor.fetchone():
        print("Erro! Já existe um usuário com esse CPF.")
        return

    while True:
        senha = input("Digite sua senha (6 dígitos): ")
        if re.match(r'^\d{6}$', senha):
            break
        else:
            print("A senha deve ter exatamente 6 dígitos.")

    numero_conta = random.randint(10000, 99999)

    # Inserir os dados do usuário e conta no banco de dados
    try:
        cursor.execute(
            "INSERT INTO usuarios (cpf, nome, data_nascimento, senha) VALUES (%s, %s, %s, %s)",
            (cpf, nome, data_nascimento, senha)
        )
        cursor.execute(
            "INSERT INTO contas (numero_conta, saldo, cpf_usuario) VALUES (%s, %s, %s)",
            (numero_conta, 0, cpf)
        )
        conexao.commit()
        print(f"Conta número {numero_conta} para o usuário {nome} criada com sucesso!\n\n")
    except mysql.connector.Error as err:
        print(f"Erro ao criar conta: {err}")
        conexao.rollback()

    cursor.close()

