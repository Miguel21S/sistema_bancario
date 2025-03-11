from datetime import datetime


SAQUE_MAXIMO = 500
LIMITE_DE_SAQUES = 3
LIMITE_DIARIO = 10

def verificar_novo_dia(ultima_data, count_saque, count_limite_diario):
    hoje = datetime.now().date()
    if hoje > ultima_data:
        return hoje, 0,0
    return ultima_data, count_saque, count_limite_diario
    
def deposito(saldo, extrato, depositar):
    if depositar <= 0:
        print("Valor inválido para depósito.")
        return saldo, extrato

    agora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    saldo += depositar
    extrato += f"\nDepósito: + R$ {depositar} {agora}"
    print(f"Depósito realizado com sucesso. Saldo atual: R$ {saldo}")
    return saldo, extrato

def levantamento(saldo, extrato, sacar, count_saque):
    if sacar <= 0:
        print("Valor inválido para saque.")
        return saldo, extrato, count_saque

    if count_saque >= LIMITE_DE_SAQUES:
        print("Você atingiu o limite máximo de saques diários (3).")
        return saldo, extrato, count_saque
    
    if sacar > saldo:
        print("Não tem saldo suficiente para realizar a operação.")
        return saldo, extrato, count_saque          
    
    if sacar > SAQUE_MAXIMO:
        print("Has superado o valor máximo de saque.")
        return saldo, extrato, count_saque
    
    agora = datetime.now().strftime("%D-%M-%Y %H:%M:%S")
    saldo -= sacar
    count_saque+=1
    extrato += f"\nSaque: - R$ {sacar} {agora}"
    print(f"Saque realizado com sucesso. saldo atual: R$ {saldo}")
    print(f"Tens direito a 3 saques diario. Número de saques: {count_saque}/3")
        
    return saldo, extrato, count_saque
        
def extrato_bancario(saldo, extrato):
    print("\n" + " EXtracto Bancario ".center(50, "="))
    print(extrato if extrato else "Nenhuma transação realizada.")
    print(f"Saldo atual: R$ {saldo}")
 
def conta_bancaria():
    saldo = 0
    extrato = ""
    count_saque = 0
    count_limite_diario = 0
    ultima_data = datetime.now().date()
    
    menu = ''' 
    Digite uma das opções
    1 Depósito o Sacar
    2 Extrato
    3 Sair
    '''
    menu_secundario = ''' 
    Digite uma das opções
    1 Depósito
    2 Saque
    3 Cancelar
    '''
    while True:
        print(menu)
        
        valor = int(input("Digite o número da operação: "))
        
        if valor == 1:
            ultima_data, count_saque, count_limite_diario = verificar_novo_dia(ultima_data, count_saque, count_limite_diario)

            if count_limite_diario >= LIMITE_DIARIO:
                print("Você atingiu o limite diário de transações (10).")
                continue
            
            while True:
                print(menu_secundario)
                valor_1_2 = int(input("Digite o número da operação: "))
                
                if valor_1_2 == 1:
                    depositar = int(input("Digite a quantia a depositar: "))
                    saldo, extrato = deposito(saldo, extrato, depositar)
                    count_limite_diario += 1
                    print(f"Limite diario: {count_limite_diario}/10")
                                    
                elif valor_1_2 == 2:
                    sacar = int(input("Digite a quantia a sacar: "))
                    saldo, extrato, nuevo_count_saque  = levantamento(saldo, extrato, sacar, count_saque)
                        
                    if nuevo_count_saque > count_saque:
                        count_limite_diario += 1  
                        count_saque = nuevo_count_saque
                        print(f"Limite diario: {count_limite_diario}/10")
                                    
                elif valor_1_2 == 3:
                    break
                
                else:
                    print("Opção inválido. Intenta de novo")
                                        
                if count_limite_diario >= LIMITE_DIARIO:
                    print("Você atingiu o limite diário de transações.")
                    break
                    
        elif valor == 2:
            extrato_bancario(saldo, extrato)
                
        elif valor == 3:
            print("Volta sempre!")
            break
        else:
            print("Opção inválido. Intenta de novo")

conta_bancaria()
