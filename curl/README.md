# CURL CheatSheet

## 1. Sending XML payload by POST
```shell
curl -X POST $URL_TO_POST -H  'Content-Type: application/xml' -d @payload.xml | xmllint --format -
```
