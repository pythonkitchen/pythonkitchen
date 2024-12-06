title: How to serve nginx from custom paths
slug: remove-committed-secrets-repository
pub: 2024-11-06 06:38:00
authors: arj
tags: 
category: devops

If you want to serve nginx from a custom location, here's what worked for me.


We give execute permissions (+x) to (others) and (groups) associated with the file or dir. Let's say our dir is `/home/ec2-user`. You can refine the path.

```
sudo chmod og+x /home/ec2-user
```

To check, see if nginx can access the files

```
sudo -u nginx ls /home/ec2-user/frontend/dist/
```

Reload nginx

```
sudo systemctl reload nginx
```