provider "aws" {
  access_key = var.aws_access_key
  secret_access_key = var.aws_secret_access_key
  region = "us-east-1"
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-bucket"
  acl    = "private"
}