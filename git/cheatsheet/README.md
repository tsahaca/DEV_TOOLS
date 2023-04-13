# Cheat Sheet

## Cleanup forked repos
1. Query to retrieve the forked repos
```bash
curl https://api.github.com/users/tsahaca/repos?per_page=100&page=1 | jq '.[] | select(.fork==true) | .clone_url' > forked-repos.txt
```
2. prepare a file like this

```text
sahaca/github-api-global-lib
tsahaca/spring-jms-examples
tsahaca/strimzi-kafka-tutorial
tsahaca/styleguide
tsahaca/terraform-k8s
tsahaca/TerraformVpcInstance
tsahaca/traefik-workshop
tsahaca/vagrant-k3s-HA-cluster
tsahaca/week-24-project
```

3. Create a Personal Access Token with **delete_repo** permission 
4. Copy the Personal Access Token
4. create a file delete_forked_repos.sh as

```bash
while read repo; do curl -X DELETE -H "Authorization: token YOUR_TOKEN" "https://api.github.com/repos/$repo"; done < forked-repos.txt
```

[Medium](https://medium.com/analytics-vidhya/delete-all-unused-github-repositories-using-github-api-18ea4d17b8e9)
