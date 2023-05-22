provider "aws" {
  access_key = var.aws_access_key
  secret_access_key = var.aws_secret_access_key
  region = "us-east-1"
}

resource "aws_instance" "my_instance" {
  ami           = "ami-0c94855ba95c71c99"
  instance_type = "t2.micro"

  tags = {
    Name = "my-instance"
  }
}
