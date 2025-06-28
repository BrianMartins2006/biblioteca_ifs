# Use a imagem oficial do Python
FROM python:3.9-slim-buster

# Define variáveis de ambiente para o Python
ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instala as dependências do sistema operacional necessárias
RUN apt-get update && apt-get install -y \
    postgresql-client \
    gcc \
    python3-dev \
    musl-dev \
    libffi-dev \
    libpq-dev \
    # Limpa o cache para reduzir o tamanho da imagem
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de requisitos e instala as dependências do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY . /app/

# Expõe a porta 8000 para o servidor de desenvolvimento do Django
EXPOSE 8000

# Comando para iniciar o servidor Django (será sobrescrito pelo docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]