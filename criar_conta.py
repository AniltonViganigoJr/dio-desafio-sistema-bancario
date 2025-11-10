def criar_nova_conta(*,
                     cpf: str,
                     lista_contas: list[dict],
                     lista_clientes: list[dict]
                     ) -> tuple[list[dict],bool]:
    
    for cliente in lista_clientes:
        if cliente['cpf'] == cpf:
            qtd_contas = len(lista_contas)
            conta = int(qtd_contas) + 1
            agencia = '0001'
            
            if not cliente.get('contas'):
                cliente['contas'] = [] 
                
            cliente['contas'].append({
                    'conta': conta,
                    'agencia': agencia
                })
            
            lista_contas.append({
                'conta': conta,
                'agencia': agencia
            })