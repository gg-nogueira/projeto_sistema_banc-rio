import mysql.connector

def confirmar_senha(cpf, senha, conexao):
    cursor = conexao.cursor()
    query = "SELECT senha FROM usuarios WHERE cpf = %s"
    cursor.execute(query, (cpf,))
    senha_banco = cursor.fetchone()[0]
    return senha == senha_banco

def depositar(cpf, conexao):
    try:
        valor = float(input("Quanto você quer depositar? "))
        if valor > 0:
            senha = input("Confirme sua senha para continuar: ")
            if confirmar_senha(cpf, senha, conexao):
                cursor = conexao.cursor()
                query = "UPDATE contas SET saldo = saldo + %s WHERE cpf_usuario = %s"
                cursor.execute(query, (valor, cpf))
                conexao.commit()

                # Adicionar ao histórico
                query_hist = "INSERT INTO historico (cpf_usuario, descricao, valor) VALUES (%s, %s, %s)"
                cursor.execute(query_hist, (cpf, 'Depósito', valor))
                conexao.commit()

                print(f"Depósito de R${valor:.2f} realizado com sucesso!")
            else:
                print("Senha incorreta. Operação cancelada.")
        else:
            print("Erro! Valor de depósito inválido.")
    except ValueError:
        print("Erro! Por favor, insira um valor numérico válido.")

def sacar(cpf, conexao):
    try:
        valor = float(input("Quanto você gostaria de sacar? (Limite de R$500) "))
        cursor = conexao.cursor()
        query_saldo = "SELECT saldo FROM contas WHERE cpf_usuario = %s"
        cursor.execute(query_saldo, (cpf,))
        saldo_atual = cursor.fetchone()[0]

        if valor > saldo_atual:
            print("Erro! Saldo insuficiente.")
        elif valor > 500:
            print("Erro! Seu limite é de R$500.")
        elif valor <= 0:
            print("Erro! Valor de saque inválido.")
        else:
            senha = input("Confirme sua senha para continuar: ")
            if confirmar_senha(cpf, senha, conexao):
                query = "UPDATE contas SET saldo = saldo - %s WHERE cpf_usuario = %s"
                cursor.execute(query, (valor, cpf))
                conexao.commit()

                # Adicionar ao histórico
                query_hist = "INSERT INTO historico (cpf_usuario, descricao, valor) VALUES (%s, %s, %s)"
                cursor.execute(query_hist, (cpf, 'Saque', -valor))
                conexao.commit()

                print(f"Saque de R${valor:.2f} realizado com sucesso!")
            else:
                print("Senha incorreta. Operação cancelada.")
    except ValueError:
        print("Erro! Por favor, insira um valor numérico válido.")

def exibir_extrato(numero_conta, cursor):
    query = """
    SELECT tipo_transacao, valor, data_hora 
    FROM historico
    WHERE numero_conta = %s
    ORDER BY data_hora;
    """
    
    cursor.execute(query, (numero_conta,))
    extrato = cursor.fetchall()

    if not extrato:
        print("Nenhuma movimentação realizada até o momento.")
    else:
        print("\nExtrato de movimentações:")
        for transacao in extrato:
            tipo, valor, data_hora = transacao
            print(f"{data_hora} - {tipo}: R${valor:.2f}")
    
    # Exibir saldo atual
    query_saldo = "SELECT saldo FROM contas WHERE numero_conta = %s;"
    cursor.execute(query_saldo, (numero_conta,))
    saldo = cursor.fetchone()[0]
    print(f"Saldo atual: R${saldo:.2f}\n")