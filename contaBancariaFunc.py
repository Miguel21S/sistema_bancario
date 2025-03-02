
menu = ''' 
Digite uma das opções
1 Deposito
2 Sacar
3 Extrato
4 Sair
'''
print(menu)

def conta_bancaria():
    SAQUE_MAXIMO = 500
    LIMITE_DE_SAQUES = 3
    saldo = 0
    count_saque = 0
    extrato = ""
    saque_total =0
    
    while True:
        valor = int(input("Digite o número da operação: "))
        if valor == 1:
            depositar = int(input("Digite a quantia a depositar: "))
            if depositar > 0:
                saldo += depositar
                extrato += f"\nDepósito: + R$ {depositar} "
                print(f"Depósito realizado successo. saldo atual: R$ {saldo}")
            else:
                    print("Valor inválido para depósito.")

        elif valor == 2:
            if count_saque < LIMITE_DE_SAQUES:
                sacar = int(input("Digite a quantia a sacar: "))

                if sacar > saldo:
                    print("Não tem saldo suficiente para realizar a operação")

                elif sacar > SAQUE_MAXIMO:
                    print("Has superado valor máximo a sacar")

                elif sacar <= saldo:
                    count_saque += 1
                    saldo -= sacar
                    extrato += f"\nSaque: - R$ {sacar} "
                    print(f"Saque realizado com sucesso. saldo atual: R$ {saldo}")
                    print(f"Tens direito a 3 saques diario. Número de saques: {count_saque}/3")
                
                else:
                        print("Valor inválido para saque.")
                 
            else:
                print("Você atingiu o limite máximo de saques diários (3).")

        elif valor == 3:
            print("\n=================== EXtracto Bancario ===================")
            print(extrato if extrato else "Nenhuma transação realizada.")
            print(f"Saldo atual: R$ {saldo}")

        elif valor == 4:
            print("Volta sempre!")
            break

        else:
            print("Opção inválido. Intenta de novo")

conta_bancaria()