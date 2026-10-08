# Organizador de Tarefas

O Organizador de Tarefas é um sistema baseado em CRUD voltado para
a gestão de tarefas do dia a dia

## Funcionalidades

- Criar tarefas com os atributos 'Nome', 'Prioridade' e 'Status';
- Editar tarefas;
- Remover tarefas;
- Listagem de tarefas com filtro;
- Controle de tarefas através de arquivo txt.

## Como rodar
1. Ter python, a partir da versão 3.10, instalado na máquina;
2. No terminal, dentro da pasta, executar:
    `python Organizador_de_tarefas_V2.py`.

## Estrutura do projeto

- `Organizador_de_tarefas_V2.py` — Arquivo main do projeto, onde todos os demais arquivos são importados para seu funcionamento;
- `CRUD` — Pasta cujos módulos utilizados no main estão hospedados;
- `CRUD/__init__.py` — Arquivo de inicialização de módulo;
- `CRUD/menu.py` - Módulo cujas funções são todas voltadas para o funcionamento principal do sistema, focando em todos os elementos do CRUD;
- `CRUD/auxiliares.py` — Módulo cujas funções são voltadas para formatação e redução de redundância dentro do módulo `CRUD/menu.py` e do main.

## Primeiro contato

Ao acessar o programa, a primeira coisa a aparecer será o menu inicial, onde o usuário poderá executar as atividades disponíveis,
conforme sua necessidade:

------------------------------------------------------------
                       MENU PRINCIPAL                       
------------------------------------------------------------

1 - Adicionar Tarefa
2 - Listar Tarefas
3 - Editar Tarefa
4 - Remover Tarefa
5 - Sair


## Sobre o projeto

Este projeto foi meu primeiro CRUD voltado para a realidade, onde pode ser utilizado para gestão de tarefas diárias com persistência em arquivo .txt.

## Autor

[Gabriel Hipólito] — [@hipolitoghm-ops](https://github.com/hipolitoghm-ops)