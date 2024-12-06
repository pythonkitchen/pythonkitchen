title: How to create an object in salesforce using Python
slug: create-object-salesforce-using-python
pub: 2024-11-06 05:56:00
authors: arj
tags: 
category: salesforce

Here's a simple snippet for creating a new custom object in Salesforce in Python.

```python
from simple_salesforce import Salesforce


sf = Salesforce(
    username='',
    password='',
    security_token='',
    domain='login'
)
try:
    mdapi = sf.mdapi
    custom_object = mdapi.CustomObject(
        fullName="Object11__c",
        label="Custom Object 1",
        pluralLabel="Custom Objects",
        nameField=mdapi.CustomField(
            label="Name__c",
            type=mdapi.FieldType("Text")
        ),
        deploymentStatus=mdapi.DeploymentStatus("Deployed"),
        sharingModel=mdapi.SharingModel("Read")
    )
    mdapi.CustomObject.create(custom_object)
except Exception as e:
    print(e)
```