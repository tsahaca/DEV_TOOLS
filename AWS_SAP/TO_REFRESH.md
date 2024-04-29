# Services and Features to Read

1. Permission boundary
2. CloudWatch Synthetic Canary - Health Check, API
3. Security Hub
4. IAM Access Analyzer and CloudTrail
5. Amazon Workspaces
6. Timestream Databases
7. Step Functions Standard vs Express
8. AWS Outpost rack vs Outpost Server
9. AWS Batch vs EMR
10. EC2 Cluster Placement Group plus reserved instances - low latency and cost effective
11. S3 Transfer acceleartion endpoint -  S3 Transfer Acceleration uses CloudFront edge locations and optimized network paths to accelerate object transfer.
12. Gigabit to Gigabyte - 1 Gigabit = 1/8 Gigabyte = .125 Gigabyte
13. Data Transfer from On-Prem to AWS - AWS Snowball Edge storage optimized devices
14. Multi-Region failover strategy for the data tier on a single EC2 instance that runs a PostgreSQL database - > Aurora global databases span multiple AWS Regions. This solution would make fast failover to another Region possible.
15. AWS Timestream Table
16. AWS App Runner to host the web application and farget too run the order processing solution

17. A company's processing team has an AWS account with a production application. The application runs on Amazon EC2 instances behind a Network Load Balancer (NLB). The EC2 instances are hosted in private subnets in a VPC in the eu-west-1 Region. The VPC was assigned the CIDR block of 10.0.0.0/16. The company's billing team recently created a new AWS account and deployed an application on EC2 instances that are hosted in private subnets in a VPC in the eu-central-1 Region. The new VPC is assigned the CIDR block of 10.0.0.0/16.

The processing application needs to communicate securely with the billing application over a proprietary TCP port.

What should a solutions architect do to meet this requirement with the LEAST operational effort?

In the billing team's account, create a new VPC and subnets in eu-west-1 that use the CIDR block of 192.168.0.0/16. In the processing team's account, create a VPC endpoint service that is powered by AWS PrivateLink. Create an interface VPC endpoint in the new VPC. Configure an inter-Region VPC peering connection in the billing team's account between the two VPCs.
