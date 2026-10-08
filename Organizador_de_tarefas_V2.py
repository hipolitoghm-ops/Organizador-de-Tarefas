# CÓDIGO REESCRITO

from CRUD.auxiliares import carregar_arquivo, salvar_arquivo, cabecalho, temporizador
from CRUD.menu import menu_principal, adicionar_tarefa, remover_tarefa, listar_tarefa, editar_tarefa, sair

lista_tarefas = []

carregar_arquivo(lista_tarefas, "tarefas.txt")

lista_menu = [('Adicionar Tarefa', lambda: adicionar_tarefa(lista_tarefas)), ('Listar Tarefas', lambda: listar_tarefa(lista_tarefas)), ('Editar Tarefa', lambda: editar_tarefa(lista_tarefas)), ('Remover Tarefa', lambda: remover_tarefa(lista_tarefas)), ('Sair', sair())]

menu_principal(lista_menu)

salvar_arquivo(lista_tarefas, 'tarefas.txt')