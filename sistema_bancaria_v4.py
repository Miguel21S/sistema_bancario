from datetime import datetime

MAX_WITHDRAWAL = 500
DRAW_LIMIT = 3
DAY_LIMIT = 10

##########################   METHOD TO CHECK IF IT'S A NEW DAY
def check_new_day(last_date, withdrawal_count, daily_count_limit):
     today = datetime.now().date()
     if today > last_date:
         return today, 0,0
     return last_date, withdrawal_count, daily_count_limit

##########################   METHOD TO CREATE USER
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

##########################   METHOD TO CREATE ACCOUNT
def creat_account_bank(agency_data, user, count, available_balance):
    # count+=1
    agency_account = {
        "Agency": input("Digite o nome do banco: "),
        "User Name": input("Digite seu nome: "),
    }
    
    agency_account["Number Account"] = "000" + count
    agency_account["Available balance"] = available_balance
    if not any(us["name"] == agency_account["User Name"] for us in user):
        print("Este usuário não está cadastrado")
        return agency_data
    
    if any(account["Number Account"] == agency_account["Number Account"] for account in agency_data):
        print(f"O nº da conta já existe na BD")
    else:
        agency_data.append(agency_account)
        print("Conta criada com successo")
         
    return f"\nEstou dentro: {agency_data}"

##########################   METHOD FOR FILTERING USER IN ACCOUNT
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

##########################   METHOD TO LIST USERS AND METHOD TO LIST ACCOUNTS
def list_account_and_users(accounts_users):
    if accounts_users:
        print("\n Lista de cadastrada:")
        for u in accounts_users:
            print(u)
    else:
        print("\nNão há registros de cadastrados.")
    
##########################   DEPOSIT METHOD 
def deposited(extract, number_account, account, deposit):
    check_account = next((count for count in account if count["Number Account"] == number_account), None)

    if not check_account:
        print("Esta conta não existe.")
        return check_account["Available balance"], extract

    if deposit <= 0:
        print("Valor inválido para depósito.")
        return check_account["Available balance"], extract

    today = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    check_account["Available balance"] += deposit

    extract += f"\nDepósito: + R$ {deposit} {today}"
    print(f"Depósito realizado com sucesso. Saldo atual: R$ {check_account['Available balance']}")

    return check_account["Available balance"], extract

##########################   WITHDRAW METHOD 
def withdrawal(extract="", withdraw=0, withdrawal_count=0, number_account="", account=[]):
    check_account = next((count for count in account if count["Number Account"] == number_account), None)

    if not check_account:
        print("Esta conta não existe.")
        return check_account["Available balance"], extract, withdrawal_count

    if withdraw <= 0:
        print("Valor inválido para saque.")
        return check_account["Available balance"], extract, withdrawal_count

    if withdrawal_count >= DRAW_LIMIT:
        print("Você atingiu o limite máximo de saques diários (3).")
        return check_account["Available balance"], extract, withdrawal_count

    if withdraw > check_account["Available balance"]:
        print("Não tem saldo suficiente para realizar a operação.")
        return check_account["Available balance"], extract, withdrawal_count

    if withdraw > MAX_WITHDRAWAL:
        print("Has superado o valor máximo de saque.")
        return check_account["Available balance"], extract, withdrawal_count

    today = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    check_account["Available balance"] -= withdraw
    withdrawal_count += 1

    extract += f"\nSaque: - R$ {withdraw} {today}"
    print(f"Saque realizado com sucesso. Saldo atual: R$ {check_account['Available balance']}")
    print(f"Tens direito a 3 saques diarios. Número de saques: {withdrawal_count}/3")

    return check_account["Available balance"], extract, withdrawal_count

##########################   METHOD TO EXTRACT BANK STATEMENT       
def bank_statement(credit_balance, extract = ""):
    print("\n" + " Extracto Bancario ".center(50, "="))
    print(extract if extract else "Nenhuma transação realizada.")
    print(f"Saldo atual: R$ {credit_balance}")
 
def account_bank():
    user = []
    # cbf = []
    account = []
    count = 0
    credit_balance = 0
    extract = ""
    withdrawal_count = 0
    daily_count_limit = 0
    last_date = datetime.now().date()
    
    menu = ''' 
    Digite uma das opções
    \t1 - Criar usuario
    \t2 - Criar conta
    \t3 - Depósito o Levantamento
    \t4 - Listar Contas
    \t5 - Listar Usuários
    \t6 - Filtrar
    \t7 - extracto
    \t8 - Sair
    '''
    menu_secundario = ''' 
    Digite uma das opções
    1 Depósito
    2 Levantamento
    3 Cancelar
    '''
    while True:
    
        try:
            print(menu)
            valor = int(input("Digite o número da operação: "))
        except ValueError:
            print("Opção inválida! Digite um número.")
            continue
        
        if valor == 1:
            create_user(user)
                    
        elif valor == 2:
            count += 1
            creat_account_bank(account, user, str(count), credit_balance)
                
        elif valor == 3:
            last_date, withdrawal_count, daily_count_limit = check_new_day(last_date, withdrawal_count, daily_count_limit)

            if daily_count_limit >= DAY_LIMIT:
                print("Você atingiu o limite diário de transações (10).")
                continue
            
            while True:
                print(menu_secundario)
                valor_1_2 = int(input("Digite o número da operação: "))
                
                if valor_1_2 == 1:
                    number_account = input("Digite o nº da conta: ")
                    deposit = int(input("Digite a quantia a depositar: "))
                    credit_balance, extract = deposited(extract, number_account, account, deposit)
                    daily_count_limit += 1
                    print(f"Limite diario: {daily_count_limit}/10")
                                    
                elif valor_1_2 == 2:
                    number_account = input("Digite o nº da conta: ")
                    withdraw = int(input("Digite a quantia a levantar: "))
                    credit_balance, extract, new_withdrawal_count = withdrawal(extract, withdraw, withdrawal_count, number_account, account)
                        
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
        elif valor == 4:
            list_account_and_users(account)
        elif valor == 5:
            list_account_and_users(user)
        elif valor == 6:
            cbf = input("Filtra o cbf: ")
            filter_user_in_account(cbf, user, account)
        elif valor == 7:
            bank_statement(credit_balance, extract)

        elif valor == 8:
            print("Volta sempre!")
            break
        else:
            print("Opção inválido. Intenta de novo")

account_bank()