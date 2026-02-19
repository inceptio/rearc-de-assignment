resource "aws_s3_bucket" "bls_bucket" {
  bucket = var.bucket_name
}

# Disable block public access
resource "aws_s3_bucket_public_access_block" "public_access" {
  bucket = aws_s3_bucket.bls_bucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

# Public Read Policy
resource "aws_s3_bucket_policy" "public_policy" {
  bucket = aws_s3_bucket.bls_bucket.id

  depends_on = [aws_s3_bucket_public_access_block.public_access]

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [

      # Public Read Access
      {
        Sid       = "PublicRead"
        Effect    = "Allow"
        Principal = "*"
        Action    = "s3:GetObject"
        Resource  = "${aws_s3_bucket.bls_bucket.arn}/*"
      },

      # Allow specific IAM user to upload
      {
        Sid    = "AllowS3UserUpload"
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::407444510398:user/s3_user"
        }
        Action = [
          "s3:PutObject",
          "s3:GetObject",
          "s3:ListBucket"
        ]
        Resource = [
          aws_s3_bucket.bls_bucket.arn,
          "${aws_s3_bucket.bls_bucket.arn}/*"
        ]
      }

    ]
  })

}
