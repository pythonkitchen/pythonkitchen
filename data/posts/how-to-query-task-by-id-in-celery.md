title: How to query task by id in celery
slug: how-to-query-task-by-id-in-celery
pub: 2021-08-15 07:27:43
authors: arj
tags: celery, debugging, task management
category: distributed systems
related_posts: how-to-set-task-id-in-celery,celery-task-asyncresult-no-attribute,how-to-define-prefect-deployment

Using celery 5.1.2 you can get the task id by the following code snippet:


```python
from celery import current_app as celery_app

# in your function:
celery_app.tasks['task_dosomething'].AsyncResult('task_id')


```


Where task\_dosomething is the name of your task and task\_id is the id you choose. You can learn more about setting task id [here](https://www.pythonkitchen.com/how-to-set-task-id-in-celery/)

Works on windows 8
