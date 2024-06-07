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
        valor_deposito = float(input("Qual o valor que deseja depositar? "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"\nDepósito: R${valor_deposito:.2f}"
        else:
            print("Valor informado não é válido")
    elif opcao == "s":
        if saldo <= 0:
            print("Não é possível sacar o dinheiro por falta de saldo")
        else: 
            while numero_saques < LIMITE_SAQUES:
                valor_saque = float(input("Qual o valor que deseja sacar? "))
                if valor_saque > 0 and valor_saque <= limite:
                    if valor_saque <= saldo:
                        saldo -= valor_saque
                        numero_saques += 1
                        extrato += f"\nSaque: R${valor_saque:.2f}"
                        print("Saque realizado com sucesso!!!")
                        continuar = input("Deseja realizar mais um saque? (digite 'sim' ou 'nao') ")
                        if continuar.lower() == "nao":
                            break
                        else:
                            continue      
                    else:
                        print("Saldo insuficiente para realizar o saque")
                        break
                else:
                    print("O valor limite do saque é 500R$ e deve ser positivo")
                    break
            if numero_saques >= LIMITE_SAQUES:
                print("Você atingiu o número máximo de saques diários")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}\n")
        print("==========================================")
    elif opcao == "q":
        break
    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    