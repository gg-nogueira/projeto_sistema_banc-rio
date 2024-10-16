def confirmar_operacao():
    """Solicita confirmação do usuário para continuar a operação."""
    while True:
        resposta_senha = input("Digite sua senha para confirmar: ").strip()
        return resposta_senha


def depositar(conta, confirmacao):
    try:
        valor = float(input("Quanto você quer depositar? ").strip())
        if valor > 0:
            if confirmar_operacao()==confirmacao:
                conta['saldo'] += valor
                conta['historico'].append(f"Depósito: +R${valor:.2f}")
                print(f"Depósito de R${valor:.2f} realizado com sucesso!")
            else:
                print("Senha incorreta")
        else:
            print("Erro! Valor de depósito inválido.")
    except ValueError:
        print("Erro! Por favor, insira um valor numérico válido.")

def sacar(conta, confirmacao):
    try:
        valor = float(input("Quanto você gostaria de sacar? (Limite de R$500) ").strip())
        if valor > conta['saldo']:
            print("Erro! Saldo insuficiente.")
        elif valor > 500:
            print("Erro! Seu limite é de R$500.")
        elif valor <= 0:
            print("Erro! Valor de saque inválido.")
        else:
            conta['saldo'] -= valor
            conta['historico'].append(f"Saque: -R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
    except ValueError:
        print("Erro! Por favor, insira um valor numérico válido.")

def exibir_extrato(conta):
    if not conta['historico']:
        print("Nenhuma movimentação realizada até o momento.")
    else:
        print("\nExtrato de movimentações:")
        for transacao in conta['historico']:
            print(transacao)
    print(f"Saldo atual: R${conta['saldo']:.2f}\n")
