# MÓDULO 'AUXILIARES'

from operator import itemgetter
from time import sleep

def cabecalho(msg):
    print('\n')
    print('-'*60)
    print(msg.upper().center(60))
    print('-'*60)


def validador(msg, erro, escopo):
    
    while True:
        
        try:
             
            opc = int(input(f"\n{msg}"))
            
            if opc not in escopo:
                raise ValueError(f'{erro}')
            
            return opc
        
        except ValueError:
            print(f"\nERRO: {erro}")
                

def temporizador(msg="", tempo=0.5):
    print('\n')
    print(msg, end="")
    for _ in range (0,3): 
        print(".",end="")
        sleep(tempo)
    print('\n')


def tarefas_ordenadas(lista_tarefas):
    
    
    if not lista_tarefas:
            

            return lista_tarefas
    
    ranking = sorted(lista_tarefas, key=itemgetter('status', 'prioridade'))
        
    for numerador, tarefa in enumerate(ranking):
        
        print(f"{numerador+1} - {tarefa}")
                
    return ranking
        
        
def carregar_arquivo(lista_tarefas, nome_arquivo):
    
    try:
        
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            
            for linha in arquivo:
                
                linha = linha.strip()
                
                if not linha:
                    continue
                dados = linha.split(";")
                dados[1] = int(dados[1])
                tarefa = {"nome": dados[0], "prioridade": dados[1], "status": dados[2]}
                lista_tarefas.append(tarefa)
    
    except FileNotFoundError:
        pass
    
    return lista_tarefas
                
                


def salvar_arquivo(lista_tarefas, nome_arquivo):

        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            for tarefa in lista_tarefas:
                arquivo.write(str(tarefa['nome']) + ';' + str(tarefa['prioridade']) + ';' + str(tarefa['status']) + '\n')
