# Sistema de Biblioteca IFSULDEMINAS - Campus Machado

Este é um sistema web robusto e moderno para o gerenciamento e consulta de acervos de biblioteca, desenvolvido para otimizar o acesso a materiais e o controle de empréstimos no IFSULDEMINAS - Campus Machado.

## 🚀 Tecnologias Utilizadas

O sistema foi construído utilizando as seguintes tecnologias:

* **Python:** Linguagem de programação principal.
* **Django:** Framework web de alto nível para desenvolvimento rápido e seguro.
* **Docker:** Para conteinerização da aplicação e do banco de dados, garantindo ambiente consistente e fácil implantação.
* **Docker Compose:** Para orquestrar os múltiplos serviços (aplicação web e banco de dados).
* **PostgreSQL:** Sistema gerenciador de banco de dados relacional, robusto e escalável.
* **HTML5, CSS3, JavaScript (JQuery):** Para a interface do usuário (frontend).

## ✨ Funcionalidades

O sistema oferece as seguintes funcionalidades principais, separadas por perfil de usuário:

### **👤 Para Alunos**

* **Login e Registro:** Acesso seguro ao sistema com contas individuais.
* **Consulta e Busca de Livros:** Pesquisa de livros por título, autor, gênero e curso relacionado.
* **Filtro de Livros:** Opções de filtro por gênero e curso para refinar a busca.
* **Verificação de Disponibilidade:** Visualização rápida do status (disponível/emprestado) e previsão de devolução dos livros.
* **Meus Empréstimos:** Acompanhamento dos livros atualmente emprestados pelo próprio aluno.

### **📚 Para Bibliotecários**

* **Login:** Acesso com permissões administrativas.
* **Gerenciamento de Livros (CRUD):**
    * **Cadastrar Livro:** Adicionar novos livros ao acervo com detalhes como título, autor, gênero, curso e ano de publicação.
    * **Listar Livros:** Visualizar todo o acervo.
    * **Editar Livro:** Atualizar informações de livros existentes.
    * **Excluir Livro:** Remover livros do sistema.
* **Gerenciamento de Empréstimos:**
    * **Realizar Empréstimo:** Registrar empréstimos de livros a alunos, com controle de data de devolução prevista.
    * **Devolver Livro:** Registrar a devolução de livros, atualizando sua disponibilidade.
    * **Empréstimos Ativos:** Visualizar todos os empréstimos em andamento.
    * **Livros em Atraso:** Identificar rapidamente livros com a data de devolução excedida.
* **Gerenciamento de Usuários (Frontend):**
    * **Cadastrar Novo Usuário:** Criar contas para novos alunos ou outros bibliotecários diretamente pela interface web.
    * **Listar Usuários:** Visualizar todos os usuários cadastrados no sistema.
    * **Editar Usuário:** Modificar dados básicos de contas de usuários, incluindo o status de bibliotecário.
    * **Excluir Usuário:** Remover contas de usuários do sistema (com restrição de auto-exclusão).

## ⚙️ Como Configurar e Rodar o Projeto

Siga os passos abaixo para configurar e executar a aplicação em seu ambiente local utilizando Docker.

### **Pré-requisitos**

Certifique-se de ter os seguintes softwares instalados em sua máquina:

* **Git:** Para clonar o repositório.
* **Docker Desktop:** Inclui Docker Engine e Docker Compose.

### **Instalação e Execução**

1.  **Clone o Repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd nome_da_pasta_do_projeto # Ex: cd biblioteca_web
    ```
    *Substitua `<URL_DO_SEU_REPOSITORIO>` pela URL real do seu repositório Git.*

2.  **Crie o arquivo `.env`:**
    Na raiz do projeto (`biblioteca_web/`), crie um arquivo chamado `.env` e adicione as seguintes variáveis de ambiente:
    ```
    DB_NAME=biblioteca_db
    DB_USER=bibliotecario
    DB_PASSWORD=minhasenhaforte # Mude para uma senha segura
    SECRET_KEY=sua_chave_secreta_aqui_gerar_uma_nova # Gere uma chave secreta para produção!
    ```
    Para gerar uma `SECRET_KEY` segura, você pode usar Python:
    ```bash
    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
    ```
    Copie a saída e cole no `.env`.

3.  **Construa as Imagens Docker:**
    No terminal, na pasta raiz do projeto:
    ```bash
    docker-compose build
    ```

4.  **Inicie os Serviços e Aplique Migrações:**
    ```bash
    docker-compose up -d
    docker-compose exec web python manage.py migrate
    ```

5.  **Crie um Superusuário (Administrador):**
    Este usuário terá acesso ao painel de administração do Django e poderá atuar como bibliotecário.
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```
    Siga as instruções no terminal para criar seu `username` e `password`.

6.  **Acesse a Aplicação:**
    Abra seu navegador e acesse: `http://localhost:8000/`

    Você pode acessar o painel de administração em: `http://localhost:8000/admin/` com o superusuário criado.

## 🤝 Contribuições

Este projeto foi desenvolvido por:

* Lucas Antonio Ferreira Neto
* Brian Gustavo Martins
* Matheus Guedes (Orientador/Professor)


Sinta-se à vontade para contribuir com melhorias ou reportar issues!
