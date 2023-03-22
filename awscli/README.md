# AWS CLI behind Corporate firewall
Some times when you try to access aws services using cli, you get the following error message
```bash
aws s3 ls
[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:581)
```
1. Take the url (https://oidc.us-west-2.amazonaws.com/client/register) open in chrome 
2. Export the root certificate chain as "Base64-encoded ASCII, certificate chain"
![Export](images/aws-root-cert.png)
![Save](images/aws-root-chain.png)
