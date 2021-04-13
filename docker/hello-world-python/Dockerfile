#importar imagem, no caso, python
FROM python:3.8-slim-buster  
# cria diretorio
WORKDIR /app 

# copia arquivo local para dentro da imagem
COPY requirements.txt requirements.txt

# executa o comando
RUN pip3 install -r requirements.txt   

# copiando tudo do diretorio para o /app
COPY . .  

# comando para iniciar o serviço de forma padronizada (só pode ter um CMD)
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]  

# 'hello world' no terminal
#CMD [ "python3", "app.py"]  
