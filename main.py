from menu import apresentar_menu
from operacoes import *
from cliente import *
from criar_conta import *

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
lista_contas = []
lista_clientes: list[dict] = []
extrato: list[str] =  []

while True:
    opcao = input(apresentar_menu())

    if opcao == "d":
        valor: float = input("Informe o valor do depósito: ")

        if valor > 0:
            saldo, extrato = depositar(valor, saldo, extrato)
        else:
            print("Operação falhou! O valor informado é inválido.")
            
    elif opcao == "s":
        valor: float = input("Informe o valor do saque: ")
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        
        elif valor > 0:
            saldo, numero_saques, extrato = sacar(
                                saldo= saldo,
                                valor=valor,
                                numero_saques=numero_saques, 
                                extrato=extrato
                                )
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "c":
        cpf = str(input("Informe o CPF do cliente: "))
        existe: bool = cliente_existe(cpf=cpf, lista_clientes=lista_clientes)
        
        if not existe:
            nome: str = input("Informe o nome do cliente: ")
            data_nascimento: str = input("Informe a data de nascimento (dd/mm/aaaa): ")
            endereco: str = input("Informe o endereço (logradouro, num - bairro - cidade/sigla estado): ")
            
            lista_clientes = cadastrar_cliente(
                cpf=cpf,
                nome=nome,
                data_nascimento=data_nascimento,
                endereco=endereco,
                lista_clientes=lista_clientes)
        else:
            print("Cliente já cadastrado!")    
        
    elif opcao == "n":
        cpf = str(input("Informe o CPF do cliente: "))
        existe: bool = cliente_existe(cpf=cpf, lista_clientes=lista_clientes)
        if existe:
            criar_nova_conta(cpf=cpf, lista_clientes=lista_clientes, lista_contas=lista_contas)
        else:
            print("CPF não encontrado na lista de clientes! Realize o cadastro!") 
               
    elif opcao == "l":
        if lista_clientes:
            listar_clientes(lista_clientes=lista_clientes)
        else:
            print("Nenhum cliente cadastrado!")

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
