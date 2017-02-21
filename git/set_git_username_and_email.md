##Set git username and email

for current repo:
```bash
git config user.name
git config user.email
```

globally:
```bash
git config --global user.name
git config --global user.email
```

via editing `.git/config`: add following:
```
[user]
    email = your@email.com
    name = yourname
```
