from datetime import datetime


MAX_WITHDRAWAL = 500
DRAW_LIMIT = 3
DAY_LIMIT = 10

def create_user(user):
    user_data = {
        "name": input("Digite seu nome: "),
        "birth_data": input("Digite sua data de nascimento (DD/MM/AAAA): "),
        "cbf": input("Digite seu CBF: "),
        "address": {
            "logrador": input("Digite seu logrador: "),
            "Nº": input("Digite nº do seu bairro: "),
            "Bairro": input("Digite seu Bairro: "),
            "Cidade": input("Digite sua cidade/inicial do estado1: "),
            }
    }
    
    if any(us["name"] == user_data["name"] for us in user):
        print("Este usuário já está cadastrado")
    elif any(cbf["cbf"] == user_data["cbf"] for cbf in user):
        print("O nº do CBF já existe")
    else:
        user.append(user_data)
        print("Usuário cadastrado com successo")
    return user

def creat_account_bank(an, user, count):
    # count+=1
    agency_account = {
        "Agency": input("Digite o nome do banco: "),
        "User Name": input("Digite seu nome: "),
    }
    
    agency_account["Number Account"] = "000" + count
    if not any(us["name"] == agency_account["User Name"] for us in user):
        print("Este usuário não está cadastrado")
        return an
    
    if any(account["Number Account"] == agency_account["Number Account"] for account in an):
        print(f"O nº da conta já existe na BD")
    else:
        an.append(agency_account)
        print("Conta criada com successo")
         
    return f"\nEstou dentro: {an}"

def filter_user_in_account(cbf, user, account):
    usuario = next((u for u in user if u["cbf"] == cbf), None)
    
    if not usuario:
        print("Usuário não encontrado.")
        return
    
    print("\n Usuário encontrado:")
    print(usuario)

    contas_do_usuario = [acc for acc in account if acc["User Name"] == usuario["name"]]
    
    if contas_do_usuario:
        print("\n Contas associadas:")
        for conta in contas_do_usuario:
            print(conta)
    else:
        print("\n Este usuário não possui contas cadastradas.")


def list_account_and_users(accounts_users):
    if accounts_users:
        print("\n Lista de cadastrada:")
        for u in accounts_users:
            print(u)
    else:
        print("\nNão há registros de cadastrados.")

    
   
def deposited(credit_balance, extract, deposit):
    if deposit <= 0:
        print("Valor inválido para depósito.")
        return credit_balance, extract

    today = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    credit_balance += deposit
    extract += f"\nDepósito: + R$ {deposit} {today}"
    print(f"Depósito realizado com sucesso. saldo atual: R$ {credit_balance}")
    return credit_balance, extract

def withdrawal(credit_balance = "credit_balance", extract = "extract", withdraw = "withdraw", withdrawal_count = "withdrawal_count"):
    if withdraw <= 0:
        print("Valor inválido para saque.")
        return credit_balance, extract, withdrawal_count

    if withdrawal_count >= DRAW_LIMIT:
        print("Você atingiu o limite máximo de saques diários (3).")
        return credit_balance, extract, withdrawal_count
    
    if withdraw > credit_balance:
        print("Não tem saldo  suficiente para realizar a operação.")
        return credit_balance, extract, withdrawal_count          
    
    if withdraw > MAX_WITHDRAWAL:
        print("Has superado o valor máximo de saque.")
        return credit_balance, extract, withdrawal_count
    
    today = datetime.now().strftime("%D-%M-%Y %H:%M:%S")
    credit_balance -= withdraw
    withdrawal_count+=1
    extract += f"\nSaque: - R$ {withdraw} {today}"
    print(f"Saque realizado com sucesso. saldo atual: R$ {credit_balance}")
    print(f"Tens direito a 3 saques diario. Número de saques: {withdrawal_count}/3")
        
    return credit_balance, extract, withdrawal_count
        
def bank_statement(credit_balance, extract = "extract"):
    print("\n" + " Extracto Bancario ".center(50, "="))
    print(extract if extract else "Nenhuma transação realizada.")
    print(f"Saldo atual: R$ {credit_balance}")
 
def account_bank():
    credit_balance = 0
    extract = ""
    withdrawal_count = 0
    daily_count_limit = 0
    last_date = datetime.now().date()
    
    menu = ''' 
    Digite uma das opções
    1 Depósito o Levantamento
    2 extracto
    3 Sair
    '''
    menu_secundario = ''' 
    Digite uma das opções
    1 Depósito
    2 Levantamento
    3 Cancelar
    '''
    while True:
        print(menu)
        
        valor = int(input("Digite o número da operação: "))
        
        if valor == 1:
            last_date, withdrawal_count, daily_count_limit = check_new_day(last_date, withdrawal_count, daily_count_limit)

            if daily_count_limit >= DAY_LIMIT:
                print("Você atingiu o limite diário de transações (10).")
                continue
            
            while True:
                print(menu_secundario)
                valor_1_2 = int(input("Digite o número da operação: "))
                
                if valor_1_2 == 1:
                    deposit = int(input("Digite a quantia a depositar: "))
                    credit_balance, extract = deposited(credit_balance, extract, deposit)
                    daily_count_limit += 1
                    print(f"Limite diario: {daily_count_limit}/10")
                                    
                elif valor_1_2 == 2:
                    withdraw = int(input("Digite a quantia a levantar: "))
                    credit_balance, extract, new_withdrawal_count  = withdrawal(credit_balance, extract, withdraw, withdrawal_count)
                        
                    if new_withdrawal_count > withdrawal_count:
                        daily_count_limit += 1  
                        withdrawal_count = new_withdrawal_count
                        print(f"Limite diario: {daily_count_limit}/10")
                                    
                elif valor_1_2 == 3:
                    break
                
                else:
                    print("Opção inválido. Intenta de novo")
                                        
                if daily_count_limit >= DAY_LIMIT:
                    print("Você atingiu o limite diário de transações.")
                    break
                    
        elif valor == 2:
            bank_statement(credit_balance, extract)
                
        elif valor == 3:
            print("Volta sempre!")
            break
        else:
            print("Opção inválido. Intenta de novo")

account_bank()