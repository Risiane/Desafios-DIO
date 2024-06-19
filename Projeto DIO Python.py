saldo = 0
extrato = ""
limite_saque = 500
LIM_SAQUE__DIA = 3
saques_realizados = 0

while True:
    print("""
------------------------
    CAIXA ELETRÔNICO  
------------------------
      
    >MENU INICIAL<
      
1 - DEPOSITAR
2 - SACAR
3 - EXTRATO      
0 - ENCERRAR OPERAÇÃO
      
------------------------""")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        deposito = float(input("Informe o valor que deseja depositar: R$"))

        if deposito > 0:
            saldo += deposito
            print("Depósito realizado com sucesso.")
            extrato += f"Crédito R$ {deposito:.2f}\n"
        else:
            print("Operação negada. O valor de depósito deve ser acima de ZERO.")

    elif opcao == 2:
        if saques_realizados < LIM_SAQUE__DIA:
            saque = float(input("Informe o valor que deseja sacar: R$"))

            if saque > 0 and saque <= saldo and saque <= limite_saque:
                saldo -= saque
                extrato += f"Débito R$ {saque:.2f}\n"
                saques_realizados += 1
                print("Saque realizado com sucesso.")
            elif saque > limite_saque:
                print("Operação negada. O valor ultrapassou o limite permitido para saque.")
            elif saque > saldo:
                print("Operação negada. Saldo insuficiente.")
            else:
                print("Operação negada. O valor de saque deve ser acima de ZERO.")
        else:
            print("Operação negada. Limite de saques diários foi ultrapassado.")

    elif opcao == 3:
        print("""
------------------------
        EXTRATO
------------------------""")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"""     
Saldo atual: R$ {saldo:.2f}
------------------------""")

    elif opcao == 0:
        print("Operação finalizada. Agradecemos a preferência! \n")
        break

    else:
        print("Operação negada. Selecione uma das opções do MENU INICIAL.")