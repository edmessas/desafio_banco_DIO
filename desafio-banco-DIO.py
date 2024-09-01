menu = """Bem-vindo ao DIO Bank!
Por favor selecione a ação desejada:
[1] Depositar
[2] Sacar
[3] Ver extrato
[0] Encerrar atendimento
             
Ação desejada:    
"""

saldo = 0
extrato = []
numeroSaques = 0
limiteDeSaques = 3


def deposito(valor):
    global saldo
    saldo += valor
    print(f"Deposito de R${valor: .2f} realizada com sucesso!")
    extrato.append(f"+{valor: .2f}")
    return saldo

def saque(valor):
    global saldo, numeroSaques
    saldo -= valor
    numeroSaques += 1
    print(f"Saque de R${valor: .2f} realizada com sucesso!")
    extrato.append(f"-{valor: .2f}")
    return saldo, numeroSaques

def verExtrato():
    print("Segue o extrato da conta:\n")
    for i in range(len(extrato)):
        print(extrato[i],"\n")
    print(f"O saldo final é de R${saldo: .2f}")

while True:

    opcao = input(menu)

#Opção Depósito
    if opcao == "1":
        valor_deposito = float(input("Indique a quantidade que deseja depositar: "))
        while valor_deposito <= 0:
            print("Valor inválido, indique um valor de depósito maior que zero.")
            valor_deposito = float(input("Indique a quantidade que deseja depositar: "))
        else:
            deposito(valor_deposito)

#Opção Saque
    elif opcao == "2":
        if numeroSaques >= 3:
            print("Quantidade de saques diária excedida. \n")
        else:
            valor_saque = float(input("Indique a quantidade que deseja sacar: "))
            while valor_saque <= 0 or valor_saque > 500 or valor_saque > saldo:
                if valor_saque <= 0:
                    print("Valor inválido, indique um valor de depósito maior que zero.\n\n")
                elif valor_saque > 500:
                    print("O valor de saque ultrapassa o limite de R$500,00.\nDigite um valor aceitável.\n")
                else:
                    print("Você não possui saldo suficiente para essa ação.\nDigite um valor aceitável.\n")
                valor_saque = float(input("Indique a quantidade que deseja sacar: "))
            else:
                saque(valor_saque)

#Opção ver extrato
    elif opcao == "3":
        verExtrato()

#Opção sair
    elif opcao == "0":
        print("Atendimento encerrado, tenha um bom dia!")
        break
    else:
        print("Operação inválida, por favor selecione uma opção válida.")