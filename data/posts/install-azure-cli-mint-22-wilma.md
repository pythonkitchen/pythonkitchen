title: How to Install Azure Cli on Linux Mint 22 / Wilma
slug: install-azure-cli-mint-22-wilma
pub: 2025-01-08 15:54:02
authors: arj
tags: azure


Follow any installing azure cli on Linux mint tutorial, but, on the step below add noble main instead of something as generic as jammy main. [See comparison](https://linuxmint.com/download_all.php)


```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/azure-cli/ noble main" | sudo tee /etc/apt/sources.list.d/azure-cli.list
deb [arch=amd64 signed-by=/etc/apt/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/azure-cli/ noble main
```

## Full instructions

```
sudo apt update
sudo apt upgrade
sudo apt install apt-transport-https ca-certificates curl gnupg lsb-release
curl -sLS https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | sudo tee /etc/apt/keyrings/microsoft.gpg > /dev/null
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/azure-cli/ noble main" | sudo tee /etc/apt/sources.list.d/azure-cli.list
deb [arch=amd64 signed-by=/etc/apt/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/azure-cli/ noble main
sudo apt update
sudo apt install azure-cli -y
az --version
```
