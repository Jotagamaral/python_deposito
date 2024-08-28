menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor que você deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Seu depósito foi de: R$ {valor:.2f}\n"

        else:
            print("Não foi possível completar a transação!")

    elif opcao == "s":
        valor = float(input("Digite o valor que você deseja sacar: "))

        if valor > saldo:
            print("Não foi possível completar a transação! Você não tem saldo suficiente.")

        elif valor > limite:
            print("Não foi possível completar a transação! Valor excedeu o limite.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Não foi possível completar a transação! Saques diários excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Seu saque foi de: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Não foi possível completar a transação!")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Selecione novamente a operação desejada.")
