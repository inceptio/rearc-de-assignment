variable "aws_region" {
  default = "us-east-1"
}

variable "bucket_name" {
  description = "rearc_de_assignment"
}

variable "lambda_function_name" {
  default = "rearc-bls-census-pipeline"
}