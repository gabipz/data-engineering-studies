# importar imagem, no caso, python
FROM python:3.8-slim-buster  
# cria diretorio
WORKDIR /app 

# copia arquivo local para dentro da imagem
COPY requirements.txt requirements.txt

# executa o comando
RUN pip3 install -r requirements.txt   

# copiando tudo do diretório para o /app
COPY . .  

# criando variáveis ambiente
ENV string=abc
ENV float=0.1
ENV integer=1
ENV boolean=True

# comando para iniciar o serviço de forma padronizada (só pode ter um CMD)
CMD [ "python3", "exercicios.py"]