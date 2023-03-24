# How Installation, Configure & Use

## [Introduction](https://blog.gruntwork.io/an-introduction-to-terraform-f17df9c6d180#3fd2)
## [tfenv - Terraform Version Manager](https://spacelift.io/blog/terraform-version-upgrade)
## [Installation with tfenv](https://technology.doximity.com/articles/terraform-s3-backend-best-practices)
```bash
git clone --depth=1 https://github.com/tfutils/tfenv.git ~/.tfenv
echo 'export PATH="$HOME/.tfenv/bin:$PATH"' >> ~/.bash_profile
tfenv -v
tfenv list-remote
tfenv install 1.4.2
tfenv use 1.4.2
terraform -v
```
## [Terraform Variables](https://spacelift.io/blog/terraform-tfvars)
## Prerequisites
1. export AWS_PROFILE
2. export AWS_REGION or AWS_DEFAULT_REGION
3. terraform init
4. terraform validate
5. terraform apply
6. terraform destroy

## [How to manage multiple environments with Terraform](https://blog.gruntwork.io/how-to-manage-multiple-environments-with-terraform-32c7bc5d692)

## [How to Manage Multiple Terraform Environments Efficiently](https://spacelift.io/blog/terraform-environments)
