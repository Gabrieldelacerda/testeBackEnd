#Aqui, usamos uma imagem base oficial do Python com a versão 3.8
FROM python:3.8-slim

#Aqui, definimos o diretório de trabalho dentro do contêiner
WORKDIR /app

#Copiamos o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt requirements.txt

#Instalamos as dependências
RUN pip install --no-cache-dir -r requirements.txt

#Copiamos todo o conteúdo do diretório atual para o diretório de trabalho no contêiner
COPY . .

#Aqui, vamos expor a porta 8080
EXPOSE 8080

#Finalmente: Comando para rodar a aplicação
CMD ["python", "app.py"]