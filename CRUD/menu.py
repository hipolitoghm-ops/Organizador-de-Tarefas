# MÓDULO 'MENU'

from CRUD.auxiliares import validador, tarefas_ordenadas, temporizador, salvar_arquivo, cabecalho
from operator import itemgetter

def menu_principal(lista_menu):
    """Exibe um menu interativo e executa a função escolhida pelo usuário.

    Args:
        lista_menu (list): Lista de tuplas no formato (texto, funcao),
            onde cada item representa uma opção do menu. O texto é
            exibido e a função é chamada quando o usuário escolhe.

    Raises:
        ValueError: _description_

    Returns:
        bool: True se o menu não foi configurado (lista vazia).
            Caso contrário, a função só retorna quando o loop
            termina (comportamento indefinido no momento).
    """
    if not lista_menu:
                print("O menu não foi configurado")
                print("Encerrando o programa", end="")
                temporizador(0.5)
                return True
    
    while True:
        
        cabecalho('MENU PRINCIPAL')
        
        for indice, item in enumerate(lista_menu):
            print(f"{indice+1} - {item[0]}")
        
        while True:
            try:
                
                opcao_menu = int(input("\nSelecione uma opção: ").strip())
                
                if opcao_menu not in range(1, len(lista_menu)+1):
                    raise ValueError("Valor não existe dentro das opções disponíveis")
                break 
            
            except ValueError as e:
                print(f"Erro: {e}. Tente novamente!")
            
        # Naturalmente a última opção será a opção 'sair'
        if len(lista_menu) == opcao_menu:
            temporizador('FINALIZANDO O PROGRAMA')
            print('VOLTE SEMPRE!')
            cabecalho('PROGRAMA FINALIZADO')
            break
        
        lista_menu[opcao_menu-1][1]()
         
    return False
               
## ├── adicionar_tarefa(lista)
def adicionar_tarefa(lista_tarefa):
        
    while True:
        temporizador('carregando', 0.3)
        cabecalho('ADICIONAR TAREFA')
        # Criação do dicionário que irá dentro da lista de termos
        tarefa = {}
        
        # Verificação e definição do valor para a chave NOME
        while True:    
            
            tarefa["nome"] = input("\nNome da tarefa: ")
            
            if tarefa["nome"].strip():
                break
            else:
                print("\nErro: O campo de nome da tarefa não pode ficar em branco. Tente novamente!\n")
            
        
        # Verificação e definição do valor para a chave PRIORIDADE    
        
        tarefa["prioridade"] = validador("""\nConsidere que a maior prioridade é 1 e a menor é 5.
Prioridade da tarefa: """, 'Digite um número inteiro válido (1 a 5). Tente novamente!', (1,2,3,4,5))

        # Definição de status

        status = validador('Status da tarefa[1 - PENDENTE / 2 - CONCLUÍDO]: ', 'Valor inválido. Apenas os valores 1-(PENDENTE) ou 2-(CONCLUÍDO) são válidos. Tente novamente!', (1, 2)) 
        
        if status == 1:
            tarefa["status"] = "PENDENTE"

        else:
            tarefa["status"] = "CONCLUÍDO"
  
            
        # Inclusão da tarefa (dicionário) na lista de tarefa
        lista_tarefa.append(tarefa)
        print("Tarefa adicionada com sucesso!")
        
        # Verificação de continuação
        
        opcao = validador("Deseja continuar adicionando tarefas(1 - SIM / 2 - NÃO)? ", 'Valor inválido. Tente novamente!', (1, 2))

        if opcao == 2:
            temporizador('VOLTANDO PARA O MENU PRINCIPAL', 0.5)
            break
        
        
## ├── listar_tarefas()
def listar_tarefa(lista_tarefas): 

    while True:

        temporizador('carregando', 0.3)
        cabecalho('LISTAGEM DE TAREFAS')
        
        verificador = 0
        
        filtro = validador("""Deseja aplicar algum filtro para a listagem de tarefas?
1 - Aplicar filtro de prioridade
2 - Aplicar filtro de Status
3 - Aplicar ambos os filtros
4 - Não aplicar filtros
5 - Sair

Selecione uma opção: """, "Digite um valor válido (1 a 5). Tente novamente!\n", (1,2,3,4,5))
        
        match filtro:
            # Primeiro caso OK
            case 1:
                
                while True:
                    verificador = 0
                
                    filtro_prioridade = validador("Deseja filtrar as tarefas por qual prioridade(1 a 5)?\nSelecione uma opção: ", "Digite um valor válido para a escolha de prioridades a ser filtrada", (1, 2, 3, 4, 5))
                    
                    cabecalho(f'Lista de tarefas com o filtro de prioridade {filtro_prioridade} aplicado')
                    
                    for tarefa in lista_tarefas:
                        if tarefa["prioridade"] == filtro_prioridade:
                            verificador += 1
                            print(f"{verificador} - {tarefa}")
                    
                    if verificador == 0:
                        print(f"\nNão existem tarefas cadastradas com prioridade {filtro_prioridade}!")
                            

                    opc = validador("Deseja continuar(1 - SIM / 2 - NÃO)?", "Valor inválido. Tente novamente!", (1,2))
                    
                    if opc == 2:
                        temporizador('carregando', 0.3)
                        break   
                        
            case 2:

                while True:
                    verificador = 0

                    filtro_status = validador('Deseja filtrar por qual status[1 - PENDENTE / 2 - CONCLUÍDO]?\nSelecione uma opção: ', 'Valor inserido inválido. Tente novamente!', (1,2))
                    
                    if filtro_status == 1:
                        status = "PENDENTE"
                    else:
                        status = "CONCLUÍDO"
                    
                    cabecalho(f"Lista de tarefas com o filtro de status {status} aplicado")

                    for tarefa in lista_tarefas:
                        if tarefa["status"] == status:
                            verificador += 1
                            print(f"{verificador} - {tarefa}")
                    if verificador == 0:
                        print("Não existem tarefas com esse status.\n")
                            
                    opc = validador("Deseja continuar(1 - SIM / 2 - NÃO)", "Valor inválido. Tente novamente!", (1,2))
                    
                    if opc == 2:
                        temporizador('carregando', 0.3)
                        break

            case 3: 
                
                while True:
                    verificador = 0
                    
                            
                    filtro_prioridade = validador('Deseja filtrar as tarefas por qual prioridade[1 a 5]?\nSelecione uma opção: ','Digite um valor válido (1 a 5). Tente novamente!', (1, 2, 3, 4, 5) )
                                
                    filtro_status = validador('Deseja filtrar as tarefas por qual status[1- PENDENTE / 2 - CONCLUÍDO]?\nSelecione uma opção: ', 'Digite um valor válido (1 ou 2)', (1, 2))
                                                            
                    if filtro_status == 1:
                        status = "PENDENTE"
                    else:
                        status = "CONCLUÍDO"
                    
                    cabecalho(f"Lista de tarefas com o filtro de status {filtro_status} - {status} aplicado")
                    
                    for tarefa in lista_tarefas:
                        if tarefa["status"] == status and tarefa["prioridade"] == filtro_prioridade:
                            print(f"- {tarefa}")
                            verificador += 1
                    
                    if verificador == 0:
                        print("\nNão existem tarefas com essa prioridade e status, respectivamente.")
                    
                    opc = validador('Deseja continuar[1 - SIM / 2 - NÃO]?\nSelecione uma opção: ', 'Valor inválido. Tente novamente!', (1,2))
                    
                    if opc == 2:
                        temporizador('carregando', 0.3)
                        break


            case 4:
                    
                    ranking = sorted(lista_tarefas, key=itemgetter('status', 'prioridade'))
                    
                    if not ranking:
                        print("Nenhuma tarefa cadastrada")
                        temporizador()
                        
                    else:
                        cabecalho('Lista de tarefas sem filtros aplicados')
                        for tarefa in ranking:
                            print(f"- {tarefa}")
                        
                    opc = validador('Deseja continuar[1 - SIM / 2 - NÃO]?\nSelecione uma opção: ', 'Valor inválido. Tente novamente!', (1,2))
                                        
                    if opc == 2:
                        temporizador('carregando', 0.3)
                        break

            case 5:
                temporizador('VOLTANDO PARA O MENU PRINCIPAL', 0.5)
                break


## ├── editar_tarefa(lista)
def editar_tarefa(lista_tarefas):

    while True:
        
        temporizador('carregando', 0.3)
        cabecalho('EDITOR DE TAREFAS')
        
        ranking = tarefas_ordenadas(lista_tarefas)
        
        if not ranking:
            print("\nNenhuma lista foi cadastrada até o momento.")
            break
        
            
        opcoes_editaveis = tuple(range(1, len(ranking)+1))
        
        edit_selecionado = validador('Digite o número correspondente à tarefa a ser editada.', 'Valor inválido. O número deve corresponder a uma das tarefas listadas. Tente novamente!', opcoes_editaveis)

        confirm = validador(f'A tarefa a ser editada é *{ranking[edit_selecionado-1]['nome']}* - [1 - SIM / 2 - NÃO]?\nConfirme a operação: ', 'Digite um valor válido. Tente novamente.', (1,2))

        if confirm == 1:
            # Edição nome
            while True:
                
                try:
                    edit_nome = input(f"\n- Nome atual: {ranking[edit_selecionado-1]['nome']}\n- Nome atualizado: ").strip()
                    
                    if not edit_nome:
                        raise ValueError("O campo de edição de nome não pode ficar vazio.")

                    ranking[edit_selecionado-1]['nome'] = edit_nome
                    break

                except ValueError as e:
                    print(f"Erro: {e}")
                    
            # Edição prioridade

            edit_prioridade = validador(f'Prioridades acessíveis: 1 - 2 - 3 - 4 - 5\n- Prioridade atual: {ranking[edit_selecionado-1]['prioridade']}\n- Prioridade atualizada: ', 'O valor correspondente à prioridade deve levar em consideração números de 1 a 5.', (1,2,3,4,5))
            ranking[edit_selecionado-1]['prioridade'] = edit_prioridade


            # Edição status
                
            edit_status = validador(f'Status acessíveis: 1 - PENDENTE / 2 - CONCLUÍDO\n- status atual: {ranking[edit_selecionado-1]['status']}\n- Status Atualizado: ', 'O valor correspondente ao status deve levar em consideração números de 1 ou 2.', (1,2))
            ranking[edit_selecionado-1]['status'] = 'PENDENTE' if edit_status == 1 else 'CONCLUÍDO'
            print("Operação concluída com sucesso!")

        else:
            print("Operação cancelada.")
        
        continuar = validador('Deseja editar outra tarefa( 1 - SIM / 2 - NÃO)?\nSelecione uma opção: ', 'Valor inválido. Tente novamente!', (1,2))
                    
        if continuar == 2:
            temporizador('VOLTANDO PARA O MENU PRINCIPAL', 0.5)
            break


## ├── remover_tarefa(lista)
def remover_tarefa(lista_tarefas):
    
    while True:

        temporizador('carregando', 0.3)
        cabecalho('REMOVEDOR DE TAREFAS')
        
        ranking = tarefas_ordenadas(lista_tarefas)
        if not ranking:
            print("\nNenhuma lista foi cadastrada até o momento.")
            break        

        opcoes_removiveis = tuple(range(1, len(ranking)+1))
        
        remover_selecionado = validador(f'Digite o número correspondente à tarefa a ser editada.', 'Valor inválido. O número deve corresponder a uma das tarefas listadas. Tente novamente!', (opcoes_removiveis))
        
        confirm = validador(f'A tarefa a ser removida será a tarefa {ranking[remover_selecionado-1]['nome']} ( 1- SIM / 2 - NÃO )?.', 'Digite um valor válido. Tente novamente', (1,2))
        
        if confirm == 1:
            
            tarefa_escolhida = ranking[remover_selecionado-1]
            lista_tarefas.remove(tarefa_escolhida)
        
        else:
            
            print('OPERAÇÃO CANCELADA.')
            
        continuar = validador('Deseja remover outra tarefa( 1 - SIM / 2 - NÃO)?', 'Valor inválido. Tente novamente!', (1,2))
        
        if continuar == 2:
            temporizador('VOLTANDO PARA O MENU PRINCIPAL', 0.5)
            break
    

def sair():
    pass