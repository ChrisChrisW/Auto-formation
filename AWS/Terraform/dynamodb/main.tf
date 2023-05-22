provider "aws" {
  access_key = var.aws_access_key
  secret_access_key = var.aws_secret_access_key
  region = "us-east-1"
}

resource "aws_dynamodb_table" "my_table" {
  name           = "my-table"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "id"
  attribute {
    name = "id"
    type = "N"
  }
}
