# Amazon EC2 

Elastic Computer Cloud (EC2) é uma máquina virtual.

Uma instância é um servidor virtual na Nuvem AWS.

SSH é o protocolo padrão para o gerenciamento remoto deste tipo de instância.

```
EC2 > Instances > Launch Instance > <selecionar máquina> 
```
[^note]

O custo das máquinas variam de região pra região (localização física chama-se Data Center). A precificação dos EUA tendem a ser mais baratas. Conforme a necessidade, você escolherá uma instância. É possível consultar os preços [aqui](https://aws.amazon.com/pt/dms/pricing/).

Toda máquina Linux para se conectar a AWS precisa de um Security Group. O tipo é SSH, protocolo TCP e o source (IP), sendo o 0.0.0.0/0, público.

<img src="../src/EC2_SecurityGroup.png" alt="EC2 Security Group"/>

(Aula 02.05)

VPC é a rede da AWD.

### Algumas ações
```
EC2 > Instances > Instance state
```
Terminate: deletar instância


## Arquitetura

<img src="../src/EC2_architecture.png" alt="EC2 Architecture"/>

O retângulo externo representa a nuvem da AWS.

O AWS Elastic Load Balancer é quem vai receber todo o tráfego, os usuários chegam apenas na porta 80/443. O tráfego que chega, é distribuído nas instâncias (App Server Instances). Se o tráfego aumenta, sobe uma nova instância. E por fim, todas as instâncias apontam para o mesmo RDS.

### Notas de rodapé

[^note]: Se você tem uma aplicação específica com recomendação que rode em determinada máquina, escolha a recomendada, caso contrário, o Amazon Linux é um Red Hat [^redhat] compilado para a Amazon. Já tem umas ferramentas, umas integrações que ajudarão no futuro.

[^redhat]: O RedHat Enterprise Linux é um sistema operacional open source e plataforma empresarial Linux líder do mercado
