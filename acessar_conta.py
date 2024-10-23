def acessar_conta(conexao):
    cursor = conexao.cursor()

    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua senha: ")

    # Buscar CPF e senha no banco de dados
    cursor.execute("SELECT nome, senha FROM usuarios WHERE cpf = %s", (cpf,))
    resultado = cursor.fetchone()
    if not resultado:
        print("Erro! Usuário não encontrado.")
        return None  

    nome_db, senha_db = resultado
    if senha != senha_db:
        print("Erro! Senha incorreta.")
        return None

    print(f"Bem-vindo, {nome_db}. Acessando sua conta...")

    # Buscar conta no banco
    cursor.execute("SELECT numero_conta, saldo FROM contas WHERE cpf_usuario = %s", (cpf,))
    conta = cursor.fetchone()
    if conta:
        numero_conta, saldo = conta
        print(f"Conta: {numero_conta} | Saldo: R${saldo:.2f}")
        return cpf, numero_conta  # Retorna o CPF e o número da conta
    else:
        print("Conta não encontrada.")
        return None