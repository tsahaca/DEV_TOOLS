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
7. Use required_version on the terraform block to restrict modules to only be deployable from specific Terraform versions to ensure state compatibility.
8. Use tgswitch and tfenv to make it easier to work with multiple versions of terragrunt and terraform respectively.
9. Use version files (.terragrunt-version and .terraform-version) in your projects to automatically switch versions depending on which module you are deploying.

## [How to manage multiple versions of Terragrunt and Terraform as a team in your IaC project](https://blog.gruntwork.io/how-to-manage-multiple-versions-of-terragrunt-and-terraform-as-a-team-in-your-iac-project-da5b59209f2d)
## [Terraform and libvirtd](https://www.youtube.com/watch?v=MdeJn1k2b8Y)
## [Source code of Terraform and libvirtd](https://github.com/gitsridhar/libvirt-terraform) 
## [Installing RKE2 with terraform on Libvirt VMs](https://www.youtube.com/watch?v=2XDvqWFRFw4)
## [Source code of Installing RKE2 with terraform on Libvirt VMs](https://github.com/hoeghh/rke2-terraform)
## [How to manage multiple environments with Terraform using Terragrunt](https://blog.gruntwork.io/how-to-manage-multiple-environments-with-terraform-using-terragrunt-2c3e32fc60a8)

## [How to manage multiple versions of Terragrunt and Terraform as a team in your IaC project](https://blog.gruntwork.io/how-to-manage-multiple-versions-of-terragrunt-and-terraform-as-a-team-in-your-iac-project-da5b59209f2d)

## [How to Manage Multiple Terraform Environments Efficiently](https://spacelift.io/blog/terraform-environments)

## [Deployment of Kubernetes, Helm and YAML files using Terraform](https://msandbu.org/deployment-of-kubernetes-helm-and-yaml-files-using-terraform/)

## [Kubectl Provider](https://registry.terraform.io/providers/gavinbunney/kubectl/latest/docs)

## [Terraform tips & tricks](https://blog.gruntwork.io/terraform-tips-tricks-loops-if-statements-and-gotchas-f739bbae55f9)

## [Managing Database Secrets In Terraform](https://dev.to/kelvinskell/how-to-manage-secrets-in-terraform-like-a-pro-14nn)

## [SOPS - short for Secret Operation s](https://blog.gitguardian.com/a-comprehensive-guide-to-sops/#:~:text=SOPS%2C%20short%20for%20Secrets%20OPerationS,editor%2C%20encryption%2C%20and%20automation)

## [Creating a Rest API with Infrastructure as Code (Terraform) & Serverless (Lambda + Python) - Part 1](https://dev.to/aws-builders/creating-a-rest-api-with-infrastructure-as-code-terraform-serverless-lambda-python-part-1-3mbp)

