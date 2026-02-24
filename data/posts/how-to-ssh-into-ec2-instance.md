title: How to SSH into AWS EC2 instance
slug: how-to-ssh-into-aws-ec2
pub: 2024-11-05 22:05:00
authors: arj
tags: aws, ec2, devops, ssh
category: cloud computing
related_posts: copy-files-to-aws-ec2,raspberry-pi-setup-establishing-ssh-connection,install-azure-cli-mint-22-wilma

## Table of Contents

- Introduction
- Ensure SSH Port 22 is Allowed
- Install SSH
- Create Key Pairs
- Download Key Pair
- Generate Public Key from `.pem` File
- Add Public Key to EC2 Instance
- Connect via SSH

## Introduction

To emulate the connect functionality of AWS, you can SSH into Amazon EC2. Ensure SSH port 22 is allowed in networking. This should be the default if you did not touch anything. If you can connect to the EC2 CLI via the connect button on the GUI, it's ok!

## Ensure SSH Port 22 is Allowed

Ensure that port 22 is open in your EC2 instance's networking configuration. This is typically enabled by default unless explicitly modified.

## Install SSH

Ensure that you have SSH installed:

```
ssh

```

## Create Key Pairs

Next, [create key pairs for your EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html).

## Download Key Pair

It’s very important to remember that the key pair can only be downloaded upon creation. Download it now. If not, create a new key pair and download the `.pem` file.

## Generate Public Key from `.pem` File

Use the following command to generate a public key from the `.pem` file:

```
ssh-keygen -y -f new-key.pem > new-key.pub

```

Then, view or copy the content of `new-key.pub`:

```
cat new-key.pub

```
## Add Public Key to EC2 Instance

Go to the AWS GUI, connect to your EC2 instance, and add the content of `new-key.pub` to the `~/.ssh/authorized_keys` file on the instance.

## Connect via SSH

You can now SSH into your instance using the following command:

```
ssh -i new-key.pem ec2-user@xxx.ap-southeast-2.compute.amazonaws.com

```

- Replace `ec2-user` with the appropriate username depending on your OS. The correct username is displayed when you connect via the GUI.  
- Replace `xxx.ap-southeast-2.compute.amazonaws.com` with your instance’s public URL.
