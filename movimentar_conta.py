def depositar(conta):
    try:
        valor = float(input("Quanto você quer depositar? "))
        if valor > 0:
            conta['saldo'] += valor
            conta['historico'].append(f"Depósito: +R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Erro! Valor de depósito inválido.")
    except ValueError:
        print("Erro! Por favor, insira um valor numérico válido.")

def sacar(conta):
    try:
        valor = float(input("Quanto você gostaria de sacar? (Limite de R$500) "))
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
