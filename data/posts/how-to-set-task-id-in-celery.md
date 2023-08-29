title: How to set task id in celery
slug: how-to-set-task-id-in-celery
pub: 2021-08-15 07:24:51
authors: arj
tags: celery
category: distributed system

Here's a convenient way to set task id in celery:


```python
import uuid # in-built in Python
task_id = str(uuid.uuid1())
task_dosomething.apply_async(task_id=task_id) 

```


task\_dosomething is your task function name.

Works on windows 8
