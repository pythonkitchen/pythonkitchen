title: How to copy files to AWS Ec2
slug: copy-files-aws-ec2
pub: 2024-11-05 22:10:00
authors: arj
tags: 
category: devops

To copy files to ec2, use the included by default scp tool in linux

## Command

First follow this tutorial to isolate issues: [ssh into the Ec2](/how-to-ssh-into-aws-ec2)

```
scp -i ~/path/to/new-key.pem -r ./path/to/copy/from/dist/ ec2-user@xxx.ap-southeast-2.compute.amazonaws.com:~/path/on/ec2
```

## Fixing forbidden errors

If you get forbidden errors, please ensure that you can [ssh into the Ec2](/how-to-ssh-into-aws-ec2).