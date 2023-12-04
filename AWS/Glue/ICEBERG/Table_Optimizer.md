# Table Optimizer

glue:GetTableOptimizer action was introduced in aswcli-2.13.36

## IAM Permission

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
             "Effect": "Allow",
             "Action": [
                 "lakeformation:GetDataAccess",
             ],
             "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:DeleteObject"
            ],
            "Resource": [
                "arn:aws:s3:::iceberg-sample-data-787567/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::iceberg-sample-data-787567"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "glue:UpdateTable",
                "glue:GetTable"
            ],
            "Resource": [
                "arn:aws:glue:us-east-1:123456789:table/default/my_iceberg_table",
                "arn:aws:glue:us-east-1:123456789:database/default",
                "arn:aws:glue:us-east-1:123456789:catalog"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:us-east-1:123456789:log-group:/aws-glue/iceberg-compaction/logs:*"
        }
    ]
}
```

1. aws glue get-table-optimizer --table-name my_iceberg_table --database-name my_db --type compaction  --catalog-id <YOUR_AWS_ACCOUNT_NUMBER>
2. aws glue get-table --name my_iceberg_table --database-name my_db
