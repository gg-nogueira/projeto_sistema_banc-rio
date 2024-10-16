import re
import random

# Expressões regulares para validação de CPF e senha
cpf_regex = re.compile(r'^\d{11}$')  # regex de CPF
senha_regex = re.compile(r'^\d{6}$')

def criar_usuario(usuarios):
    nome = input("Digite seu nome: ").strip().title()
    cpf = input("Digite seu CPF (somente números): ").strip()
    
    # Validação de CPF com regex
    if not cpf_regex.match(cpf):
        print("Erro! CPF inválido. Certifique-se de que está inserindo apenas 11 números.")
        return None

    # Verifica se o CPF já está cadastrado
    if cpf in usuarios:
        print("Erro! Já existe um usuário cadastrado com este CPF.")
        return None

    data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ").strip()

    while True:
        senha = input("Digite sua senha (6 dígitos): ").strip()
        if senha_regex.match(senha):
            break  # A senha é válida
        else:
            print("Erro! A senha deve conter exatamente 6 dígitos. Tente novamente.")

    numero_conta = random.randint(10000, 99999)  # Gerar número de conta aleatório
    
    # Cria um novo usuário
    usuarios[cpf] = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "senha": senha,
        "conta": {
            "numero": numero_conta,
            "saldo": 0,  # Saldo inicial
            "historico": []  # Histórico de movimentações 
        }
    }

    print(f"Conta número {numero_conta} para o usuário {nome} criada com sucesso!\n\n")
    return cpf, numero_conta
