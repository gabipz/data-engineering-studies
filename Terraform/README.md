# Terraform

O Terraform é uma ferramenta para auxiliar a criar, administrar, tomar conta da infraestrutura de um jeito simples.

## Instalação

## Conexão com o provedor

Para fazer a gestão do ambiente, é necessário criar um usuário no provedor para conectar e dar acesso.

### AWS

IAM > Users > Add users 

<img src="../src/terraform_adduser.png" alt="Add user AWS"/>

https://www.terraform.io/cdktf/concepts/providers-and-resources

Pra fazer o deploy do projeto, é necessário a seguinte sequência de comandos:

```terraform init``` Primeira vez do projeto
```terraform plan``` O plan é pra ver quais foram as alterações (log)
```terraform apply``` Finalmente deployar
