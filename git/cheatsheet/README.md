# Cheat Sheet

## Query to retrieve the forked repos

```bash
curl https://api.github.com/users/tsahaca/repos | jq '.[] | select(.fork==true) | .clone_url'
```
[Medium](https://medium.com/analytics-vidhya/delete-all-unused-github-repositories-using-github-api-18ea4d17b8e9)
