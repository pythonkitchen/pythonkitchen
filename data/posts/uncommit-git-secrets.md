title: How to remove committed secrets from repository
slug: remove-committed-secrets-repository
pub: 2024-11-06 06:38:00
authors: arj
tags: 
category: git


If ever you committed git secrets by mistake, besides revoking the secrets, here's what you should do.


First checkout on the main branch in the remote repository where the secret has beeen committed

```
git checkout main 
git pull origin main
```

Identify what commit it was using 

```
git log
```

Then run 

```
git reset ceg3ec1^
```


Where `ceg3ec1^` is the commit hash.

Then add the file/s you want to edit out the secret

```
git add file1
```

Then commit 

```
git commit -m "fix: typoo"
```

Then push to the repo, use force to override history.

```
git push origin source --force
```

Hope it helps!