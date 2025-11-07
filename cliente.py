import os

def cliente_existe(*,
                   cpf:str, 
                   lista_clientes:list[dict]
                   ) -> bool:
    
    """Essa função verifica se um usuário conta na lista de clientes"""
    for cliente in lista_clientes:
       if cliente['cpf'] == cpf:
           return True
       return False

def cadastrar_cliente(*,cpf: str,
                      nome: str,
                      data_nascimento:str,
                      endereco: str,
                      lista_clientes:list[dict]
                      ) -> list[dict]:
    
    """Essa função adiciona um novo usuário na lista de clientes"""
    lista_clientes.append({
        'nome': nome, 
        'cpf': cpf, 
        'data_nascimento': data_nascimento,
        'endereco': endereco})
    
    return lista_clientes

def listar_clientes(*, lista_clientes:list[dict]) -> None:
    """Essa função imprime a lista de clientes cadastrados"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("**************** CLIENTES ****************")
    for index, cliente in enumerate(lista_clientes):
        print(f"{index+1} : {cliente['nome']}")