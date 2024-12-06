title: How to serve nginx from custom paths
slug: serve-nginx-custom-paths
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

Add this inside the server block in nginx `/etc/nginx/nginx.conf`

```
...
		location / {
            root /home/ec2-user/frontend/dist/;  
            index index.html;  
            try_files $uri $uri/ /index.html;
        }
...
```

Reload nginx

```
sudo systemctl reload nginx
```
