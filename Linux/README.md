#Linux

## Comandos básicos
|Comando|Descrição |
|----------------|-----------------|
|`pwd`|Onde estou|
|`whoami`|O nome do usuário no Linux|
|`which <arquivo/comando>`|Mostra onde está|
|`ls`|Listar arquivos e diretórios|
|`ls -l`|Listar arquivos e diretórios comá to  detalhes|
|`ls -la`|"" +  mostra diretórios escondidos|
|`echo "<mensagem>"`|Imprimir algo na tela|
|`echo "<mensagem>" > bem-vindo txt`|Salva a mensagem no arquivo (sobreescreve)|
|`echo <mensagem> >> bem-vindo txt`|Adiciona linha de mensagem|
|`man <comando>`|Comando de ajuda|
|`clear` ou `Ctrl + L`||
|`cd <diretorio`|Mudar de diretório|
|`mkdir  <diretorio>`|Criar diretório|
|`rmdir  <diretorio_vazio>`|Remove diretório vazio|
|`rm <arquivo>`|Remove arquivo|
|`rm -r <diretorio>`|Remove recursivamente (todos araquivos do diretório)|
|`mv <arquivo> <diretorio>`|Colocar o arquivo dentro do diretório|
|`zip -r <nome_zip.zip> <diretorio>`|Compactar|
|`unzip <nome_zip.zip>`|Desompactar|
|`unzip -l`|Mostra o que tem dentro do zip|
|`cp arq1.txt arq2.txt`|Copiar arq1 para arq2|
|`tar -cz <diretorio> > <nome_zip.tar.gz>`|Compactar tar|
|`tar -xz < <nome_zip.tar.gz>`|Descompactar tar|
|`head -n 6 arquivo.txt`|Imprime as 6 primeiras linhas do arquivo|
|`tail -n 3 google.txt`|Imprime as 3 últimas linhas do arquivo|
|`vi arquivo.txt`|Editar o arquivo no terminal (apertar a letra `i` para editar) (Para salvar `:w`) (para sair `:q`)(sair sem salvar :q!)|
|`ps`|Processos que estão sendo executados|
|`ps -e`|Lista todos os processos do Linux|
|`ps -ef`|Lista todos os processos do Linux e os detalha|
|`ps -ef | grep firefox`|Lista detalhadamente apenas os processos que tem `firefox`|
|`pstree`|Lista processos em hierarquia|
|`kill <PID>`|Matar o programa|
|`kill -9 <PID>`|Matar forçadamente o programa|
|`top`|serve para listar os processos do Linux. A diferença entre o top e o ps é que o top atualiza as informações de tempos em tempos.|
|`killall top`|Mata todos os processos que tem `top`|
|`bg <numero>`|Joga o progrma no background|
|`sh <script>`|executar o script|
|`locate <arquivo>`|Localiza onde o software/arquivo|
|`sudo updatedb`|Atualiza a base de dados que o locate utiliza para realizar as pesquisas|
|`sudo passwd`|Altera a senha do usuário `root`|
|`env`|Todas as variáveis de ambiente|
|`sudo apt-get install <software>`|Instala softwares|
|`sudo apt-get update`|Atualiza softwares|
|`sudo apt-cache search <software>`|Busca softwares pra instalação|
|`sudo dpkg -i <software.extensao>`|Instala software baixado|
|`sudo dpkg -r <software.extensao>`|Remove software baixado|
|`./configure` `sudo apt-get install zlib1g-dev` `sudo make install`|Instala a partir do código fonte|
|``||
|``||
|``||


## Leitura de arquivos
|Comando|Descrição|
|----------------|-----------------|
|`cat arquivo?.txt`|Lê todos os arquivos que um caracter entre `arquivo` e `txt`|
|`cat arquivo*.txt`|Lê todos os arquivos que N caracteres entre `arquivo` e `txt`|
|`cat *.txt`|Lê qualqer arquivo `txt`|
|`$ cat google.txt | grep "Larry Page and Sergey Brin"`|imprimir as linhas que contêm o termo "Larry Page and Sergey Brin" do arquivo google.txt|
|``||
|``||
|``||



### Letras
|Comando|Descrição|
|----------------|-----------------|
|`-a`||
|`-b`||
|`-c`|create|
|`-d`||
|`-e`||
|`-f`|file name|
|`-g`||
|`-h`||
|``||
|``||
|``||
|``||
|``||
|``||
|`-l`|list|
|``||
|``||
|``||
|`-q`|quiet|
|``||
|`-v`|verbose|
|`-x`|extract|

|`-z`|zip|
|``||
|``||
|``||
|``||
|``||
|``||
|``||

## Ctrl

|Comando|Descrição|
|----------------|-----------------|
|`ctrl + z`|Pausa o processo|



## Exemplos
Abrir firefox:
`firefox`
Ele abrirá o firefox no terminal, travando o bash
`ctrl + z` pra parar o processo
`jobs` para mostrar o status dos processos
`bg 1` colocar no banckground

para voltar pro terminal, `fg`
