title: How to solve celery task has no attribute AsyncResult
slug: celery-task-asyncresult-no-attribute
pub: Sun, 15 Aug 2021 07:36:53 +0000

I was looking through Grinberg's [tuto](https://blog.miguelgrinberg.com/post/using-celery-with-flask) on celery and flask. I saw querying tasks by


```python
task = long_task.AsyncResult(task_id)

```


But for some reasons it was not working for me. I looked at [Flower](https://github.com/mher/flower/blob/ce5f0de7b25bc42ef9fb909340ba9fe9c8f903f0/flower/views/tasks.py#L17)'s get\_task\_by\_id which led to wrapping a tornado object. It was too complicated for me to include Tornado in my project. I browsed through celery's source and found the [query\_task](https://github.com/celery/celery/blob/3cf5072ee5f95744024f60e0f4a77eb2edb8959f/celery/worker/control.py#L106) function which led me to the `_find_requests_by_id` fucntion which led to a state file but i could not find it by inspecting my celery app. I finally found the right path and documented it under [finding task by id in celery 5.1.2](https://www.pythonkitchen.com/how-to-query-task-by-id-in-celery/).

Works on windows 8
