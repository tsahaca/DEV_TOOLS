## Installing in Windows as non admin user

. Download the .msi file from Amazon website: https://awscli.amazonaws.com/AWSCLIV2.msi
. Ue msiexec in command line to extract application from msi package:
```shell
msiexec /a %USERPROFILE%/Downloads/AWSCLIV2.msi /qb TARGETDIR=%USERPROFILE%\awscli
```
. Add to path
