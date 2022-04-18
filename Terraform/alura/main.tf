provider "aws" {
    version = "~> 2.0"
    region = "us-east-1"
}

resource "aws_instance" "dev" {
    count = 3 # número de máquinas
    ami = "ami-026..." # EC2 > Launch Instance > pegar imagem (ami)
    instance_type = "t2.macro" 
    key_name = "terraform-aws" # chave local (ssh-keygen -f terraform-aws -t rsa)
    tags = {
        Name = "dev${count}.{index}" # Criação das máquinas
    }
}
