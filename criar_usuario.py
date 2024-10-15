import re
import random

cpf_regex = re.compile(r'^\d{11}$') #regex de CPF
senha_regex = re.compile(r'^\d{6}$')

def criar_usuario(usuarios):
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF (somente números): ")
    #valida o cpf
    # if cpf_regex.search(cpf):
    #   print(f"{cpf} é válido")
    # else:
    #   print(f"{cpf} é inválido")
    #   return None

    data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")

    # Verifica se o CPF já está cadastrado
    if cpf in usuarios:
        print("Erro! Já existe um usuário cadastrado com este CPF.")
        return None

    while True:
      senha = input("Digite sua senha (6 dígitos): ")
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


