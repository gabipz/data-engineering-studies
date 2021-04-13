# Docker

O Docker é basicamente uma ferramenta que facilita o _deploy_ e a execução das aplicações por meio de containers, através de uma 'receita' (código) que define como deve ser o ambiente da aplicação desde seu sistema operacional até suas dependências.

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
