title: How to fix docker.errors.DockerException: Error while fetching server API version without using Docker Desktop
slug: fix-dockererrorsdockerexception-error-fetching-server-api-version-without-using-docker-desktop
pub: 2024-11-05 21:34:00
authors: arj
tags: docker, troubleshooting, linux
category: devops
related_posts: venv-usage-on-windows-activate-and-deactivate,install-pipx-mint-ubuntu,rye-package-manager

If you use Docker and get it running while using Docker Desktop, you might run into this error:

```
docker.errors.DockerException: Error while fetching server API version: ('Connection aborted.', FileNotFoundError(2, 'No such file or directory'))
```

That's because Docker Desktop is well, not running. What if you could run Docker without needing Docker Desktop?

Check if the service is running

```
sudo systemctl status docker
```

Verify if the Docker socket exists by running:

```
ls -l /var/run/docker.sock
output: srw-rw---- 1 root docker 0 ... /var/run/docker.sock
```

If not, start the Docker service or reinstall Docker. If `docker --version` is not around, do same.

On ubuntu/linux mint verify if you have the correct permission

```
sudo usermod -aG docker $USER
```

You can also try restarting the service

```
sudo systemctl restart docker
```

If you get when running `docker version`

```
Client: Docker Engine - Community
 Version:           27.3.1
 API version:       1.47
 Go version:        go1.22.7
 Git commit:        ce12230
 Built:             Fri Sep 20 11:41:11 2024
 OS/Arch:           linux/amd64
 Context:           desktop-linux
Cannot connect to the Docker daemon at unix:///home/appinv/.docker/desktop/docker.sock. Is the docker daemon running?
```

Then, temporarily add this env var

```
export DOCKER_HOST=unix:///var/run/docker.sock
```

Also do the above if getting 

```Dec 03 13:44:47 appinv-machine dockerd[22962]: time="2024-12-03T13:44:47.469983115+04:00" level=info msg="API listen on /run/docker.sock"```

Add permanently if fixed.

If you get an error like the below which occurs as a result of authing through Docker Desktop
```
ERROR: failed to solve: ...: failed to resolve source metadata for docker.io/...: error getting credentials - err: exec: "docker-credential-desktop": executable file not found in $PATH, out: `
ERROR: Service '...' failed to build : Build failed
```

Edit this file

```
nano ~/.docker/config.json
```

Replace `"credsStore": "desktop"` with `"credsStore": ""`

Else login throught docker hub.

Hope it helps1
