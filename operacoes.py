import os

def depositar(valor: float,
              saldo: float, 
              extrato:list[str], /
              ) -> tuple[float, list[str]]:
    
    """Essa função realiza um depósito na conta do usuário"""
    saldo += valor
    extrato.append(f"Depósito: R$ {valor:.2f}\n")
    return saldo, extrato

def sacar(*, 
          saldo: float, 
          valor:float, 
          numero_saques: int,
          extrato:list[str]
          ) -> tuple[float, int, list[str]]:
    
    """Essa função realiza um saque na conta do usuário caso haja saldo disponível,
    não tenho excedido o limite de saque, o valor não seja maior que o saldo ou o número de saques diários"""
    saldo -= valor
    extrato.append(f"Saque:    R$ {valor:.2f}\n")
    numero_saques += 1
    return saldo, numero_saques, extrato
    
def exibir_extrato(saldo: float, / , *,
                   extrato: list[str]
                   ) -> None:
    
    """Essa função exibe o extrato e o saldo do usuário no console."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n=========== EXTRATO ============')
    print('\n'.join(extrato) if extrato else 'Não foram realizadas movimentações!')
    print(f'\nSaldo:\t  R$ {saldo:.2f}')
    print('================================')
