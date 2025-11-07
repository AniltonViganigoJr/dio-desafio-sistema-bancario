import textwrap
"""Esse módulo retorna o menu utilizado no Sistema Bancário"""
def apresentar_menu() -> str:
     return textwrap.dedent("""     
        [d] Depositar
        [s] Sacar
        [c] Cadastrar Cliente
        [n] Cadastrar Nova Conta
        [e] Extrato
        [l] Listar Clientes
        [q] Sair
        => """)