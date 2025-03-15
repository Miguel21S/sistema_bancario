
SAQUE_MAXIMO = 500
LIMITE_DE_SAQUES = 3
    
def deposito(saldo, extrato, depositar):
    if depositar > 0:
        saldo += depositar
        extrato += f"\nDepósito: + R$ {depositar} "
        print(f"Depósito realizado successo. saldo atual: R$ {saldo}")
        
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

def levantamento(saldo, extrato, count_saque):
    if count_saque < LIMITE_DE_SAQUES:
        sacar = float(input("Digite a quantia a sacar: "))
        
        if sacar > saldo:
            print("Não tem saldo suficiente para realizar a operação")          
        elif sacar > SAQUE_MAXIMO:
            print("Has superado valor máximo a sacar")
            
        else:
            saldo -= sacar
            count_saque+=1
            extrato += f"\nSaque: - R$ {sacar} "
            print(f"Saque realizado com sucesso. saldo atual: R$ {saldo}")
            print(f"Tens direito a 3 saques diario. Número de saques: {count_saque}/3")
            
    else:
        print("Você atingiu o limite máximo de saques diários (3).")
        
    return saldo, extrato, count_saque
        
def extrato_bancario(saldo, extrato):
    print("\n" + " EXtracto Bancario ".center(50, "="))
    print(extrato if extrato else "Nenhuma transação realizada.")
    print(f"Saldo atual: R$ {saldo}")
 
def conta_bancaria():
    saldo = 0
    extrato = ""
    count_saque = 0
    
    menu = ''' 
    Digite uma das opções
    1 Deposito
    2 Sacar
    3 Extrato
    4 Sair
    '''
    while True:
        print(menu)
        valor = int(input("Digite o número da operação: "))
        
        if valor == 1:
            depositar = float(input("Digite a quantia a depositar: "))
            saldo, extrato = deposito(saldo, extrato, depositar)
            
        elif valor == 2:
            saldo, extrato, count_saque = levantamento(saldo, extrato, count_saque)
            
        elif valor == 3:
            extrato_bancario(saldo, extrato)
            
        elif valor == 4:
            print("Volta sempre!")
            break
        else:
            print("Opção inválido. Intenta de novo")

conta_bancaria()

