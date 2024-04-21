
# Aplicação de Telemedicina com Django (PYSTACK WEEK 10)
Este projeto consiste em uma aplicação de telemedicina desenvolvida usando o framework Django. Durante três aulas, exploramos os seguintes aspectos.

#### Projeto disponibilizado por:
https://pythonando.com.br/
https://www.youtube.com/@pythonando

## Prepação do anbiente
Estou desenvolvendo no ambiente WSL2 com Ubuntu. 
Por favor, esteja ciente de que os comandos abaixo podem variar no ambiente Windows.

## Configurações
- Python versão ^3.10
- Poetry

### Para iniciar um ambiente virtual no linux
````
poetry init
````
### Iniciar o ambiente virtual
````
poetry shell
````
### Fazer a instalação de pacotes
````
poetry add NOME_PACOTE
````

### Para iniciar o projeto no linux
````
 python3 manage.py runserver
````

## Dependências
### Instalando o Django
````
poetry add django
````
### Instalando o Pillow
````
poetry add pillow
````

## Comando que foram usados na construção do projeto
### Criando um projeto Django
O ponto no final do nome do projeto e para criar o projeto na mesma pasta de onde o comando foi dado.
````
django-admin startproject NOME_DO_PROJETO . 
````
### Criando um APP Django
Para criar um novo app no django
````
python3 manage.py startapp NOME_DO_APP
````
### Criando as tabelas do banco de dados
Comando para criar as tabelas do banco de dados que já foram instaladas junto dom o projeto.
````
python3 manage.py migrate
````
### Criando as migrations
Cria um conjunto de comandos para mais tarde ser criado as tabelas no banco de dados, como se fosse uma proparação para criação das tabelas, para depois rodar o comando 'python3 manage.py migrate' para gerar as tabelas. 
````
python3 manage.py makemigrations 
````
### Comando para criar um SuperAdmin no projeto
````
python3 manage.py createsuperuser
````