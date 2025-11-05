import textwrap
"""Esse módulo retorna o menu utilizado no Sistema Bancário"""
def apresentar_menu() -> str:
     return textwrap.dedent("""     
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
        => """)