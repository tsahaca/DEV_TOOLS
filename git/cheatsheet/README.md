# Cheat Sheet

## Query to retrieve the forked repos

```bash
curl https://api.github.com/users/tsahaca/repos | jq '.[] | select(.fork==true) | .clone_url'
```
