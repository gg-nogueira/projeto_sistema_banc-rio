from criar_usuario import criar_usuario
from exibir_menu import exibir_menu
from movimentar_conta import depositar, sacar, exibir_extrato
from acessar_conta import acessar_conta
from conectar_bd import conectar_bd
# Programa principal
# usuarios = {} inicialmente armazenada infos em um dict

conexao = conectar_bd()
cursor = conexao.cursor()

while True:
    print("""\n=== Bem-vindo ao Banco GAN ===
    1- Criar conta
    2- Acessar conta
    3- Encerrar\n""")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == '1':
        criar_usuario(conexao)

    elif opcao == '2':
        numero_conta = acessar_conta(conexao)
        if numero_conta:
            while True:
                escolha = exibir_menu()
                if escolha == '1':
                    depositar(conexao)
                elif escolha == '2':
                    sacar(conexao)
                elif escolha == '3':
                    exibir_extrato(conexao)
                elif escolha == '4':
                    print("Encerrando o acesso à conta.")
                    break
                else:
                    print("Opção inválida!")

    elif opcao == '3':
        print("Obrigado por usar o Banco GAN. Até mais!")
        break

    else:
        print("Opção inválida!")

conexao.close()
