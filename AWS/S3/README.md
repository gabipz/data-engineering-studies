# Amazon Simple Storage Service (AWS S3)

O serviço de s3 é um _web storage_, ou seja, é possível armazenar e manipular objetos na nuvem com uma alta escalabilidade, redundância de dados [^redundancia] e baixo custo.

Os dados no S3 ficam dentro de _buckets_ ("baldes", em português), que são agregações.

## Utilidades

É possível criar hospedagem estática no S3 (Static Web Host). Para isso, é necessário tornar público o acesso aos arquivos e acessar pelo endpoint criado.

## Classes de armazenamento

Ao fazer upload de arquivos, há uma configuração _Storage class_ que está relacionada ao custo e disponibilidade dos objetos armazenados.

- **Amazon S3 Standard**: esta classe têm durabilidade e disponibilidade de quase 100%, é indicada para objetos com muita frequência de acesso;
- **Amazon S3 Standard - IA**: é indicada para objetos com menores frequências de acesso, e tem um custo reduzido de armazenamento se comparado ao Standard;
- **Amazon Glacier**: a disponibilidade do dado não será imediata. (Usado pra backup ou cposas que não precisam acessar corriqueiramente)

## Notas de rodapé

[^redundancia]: Redundância de dados: duplicação de componentes para garantir serviço ininterrupto e evitar perda de dados.

## Referências

- [Alura - Amazon S3: Manipule e armazene objetos na nuvem](https://cursos.alura.com.br/course/aws-s3-manipule-e-armazene-na-nuvem)
- [Documentação Oficial](https://aws.amazon.com/pt/s3/)
