resource "aws_lambda_function" "bls_lambda" {
  function_name = var.lambda_function_name
  role          = aws_iam_role.lambda_exec_role.arn
  handler       = "main.lambda_handler"
  runtime       = "python3.9"

  filename         = "../lambda/lambda.zip"
  source_code_hash = filebase64sha256("../lambda/lambda.zip")

  timeout = 300
  memory_size = 1024

  environment {
    variables = {
      BUCKET_NAME = var.bucket_name
    }
  }
}
