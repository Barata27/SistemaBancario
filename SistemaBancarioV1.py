menu = """

[d] Depósito
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITES_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor para o Depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"

        else:
            print("Operação Falhou! Informe um valor Válido!")

    elif opcao == "s":
        valor = float(input("Informe o Valor para o Saque: "))

        excedeu_saldo = saldo < valor
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= LIMITES_SAQUES

        if excedeu_saldo:
            print("Operação Falhou! Você está com o saldo insuficiente.")

        elif excedeu_limite:
            print("Operação Falhou! O valor do saque exedeu o limite permitido.")

        elif excedeu_saques:
            print("Operação Falhou! Numero Máxino de saques atinido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f}\n"
            numero_saque += 1

        else:
            print("Operação Falhou! Informe um valor Válido!")

    elif opcao == "e":
        print("\n ====== Extrato ======")
        print("Não foi possivel realizar as movimentações. " if not extrato else extrato)
        print(f"\nSaldo de R$ {saldo:.2f} ")
        print("=========================")

    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor digite uma opção válida")
