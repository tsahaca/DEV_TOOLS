## Installing in Windows as non admin user

1. Download the .msi file from Amazon website: https://awscli.amazonaws.com/AWSCLIV2.msi
2. Use msiexec in command line to extract application from msi package:

```shell
msiexec /a %USERPROFILE%/Downloads/AWSCLIV2.msi /qb TARGETDIR=%USERPROFILE%\awscli
```
3. Add to path
