# Docker

O Docker é basicamente uma ferramenta que facilita o _deploy_ e a execução das aplicações por meio de containers através de uma 'receita' (código) que define como deve ser o ambiente da aplicação desde seu sistema operacional até suas dependências.

## Contexto da ferramenta no time
Para fazer o _setup_ do AirFlow, precisamos de uma imagem de Python no Docker.

Desta forma, nesta etapa, a pessoa tripulante no cargo de estagiário deve:

- compreender o funcionamento do Docker;
- se habituar com os comandos básicos do Docker;
- usar imagem de Python;
- garantir que os pacotes Python estejam versionados em um arquivo de requirements.

## Configurações iniciais

- [Instalação](https://web.archive.org/web/20210410033653/https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04) (atenção para a versão do sistema operacional);

- [Pós instalação](https://web.archive.org/web/20210410053910/https://docs.docker.com/engine/install/linux-postinstall/) (em alguns casos, é necessário reiniciar o computador)

- [Docker Hub](https://hub.docker.com/search?q=&type=image) - repositório com imagens já prontas para os containers.

## Criação de imagem de Python

Como em vários cenários da programação, o 'Hello World' também está presente em forma de imagem no Docker, para começar a se habituar com a ferramenta, seguir o tutorial: [Build your Python image](https://web.archive.org/web/20210402160646/https://docs.docker.com/language/python/build-images/).

## Exercícios de fixação:

1. Executar um script de python que imprima "hello world" no terminal.

2. Criar uma variável ambiente e através do Python, capturar essa variável ambiente e printar no terminal.

3. Printar o tipo de variável.

# Docker Compose

O Docker Compose é o orquestrador de containers da Docker, ou seja, ele auxilia a lidar com múltiplos containers simultaneamente. Para isso, é necessário criar um arquivo de texto YAML (acrônimo recursivo para _YAML Ain’t Markup Language_) chamado ```docker-compose.yml```, e nele nós descrevemos tudo o que queremos que aconteça para subir a nossa aplicação, todo o nosso processo de build, isto é, subir o banco, os containers das aplicações, etc.

## Configurações iniciais

Além de já ter instalado o Docker, é necessário instalar o Docker Compose, pelos seguintes comandos (utilizando o Ubuntu 20.04):

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
```
E para verificar sua versão: ```docker-compose --version```.


## Referências

- [Alura cursos - Docker Compose](https://cursos.alura.com.br/course/docker-e-docker-compose/task/29498)

- [Docker Compose](https://imasters.com.br/banco-de-dados/docker-compose-o-que-e-para-que-serve-o-que-come#:~:text=Docker%20Compose%20%C3%A9%20o%20orquestrador,mas%20os%20maestros%20somos%20n%C3%B3s!)

- [Instalação](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04)
