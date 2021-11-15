## Estruturando projetos em Python - um modelo de sistema

Esse repositório contém um modelo de projeto Python descrito neste artigo do Medium:

Para executar o projeto, siga os seguintes passos após clonar o projeto:

1. Instale o virtualenv se ainda não estiver instalado:

`pip install virtualenv`

3. Crie um venv dentro do diretório do projeto:

`python3 -m venv env`

5. Ative o venv:

`source env/bin/activate`

7. Instale os requerimentos

`pip install -r requirements.txt`

8. Execute um ou mais exemplos

`make run_api`

`make run_orders`

`make run_invoices`

Veja no artigo como executar os projetos em containers Docker.
