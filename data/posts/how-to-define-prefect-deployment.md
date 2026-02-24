title: How to Define Prefect Deployments (2026)
slug: how-define-prefect-deployments
pub: 2026-01-03 19:00:00
authors: arj
tags: prefect, automation, devops
category: data engineering
related_posts: define-prefect-deployment,how-to-query-task-by-id-in-celery,celery-task-asyncresult-no-attribute

### TL;DR: Define Prefect Deployments
*   **What**: Metadata that tells the Prefect server how and when to run a specific flow.
*   **Method**: Use `.serve()` on a flow object for local long-running processes.
*   **CLI**: Trigger runs using `prefect deployment run 'name'`.

The [Prefect](https://www.prefect.io/) documentation about deplyments are super vague. This post explains how to add deployments.

## Table of content
- Where are deployment codes located in the docs
- What is a deployment
- Define and run prefect deployments
- A minimal example
- The prefect server

#### Where are deployment codes located in the docs

Deployments are not located inside the Deployment section, but rather in the [flows section](https://docs.prefect.io/latest/concepts/flows/).

#### What is a Deployment

Typically, deployments, whererver you define them, populate a class like this which you don't need to write:

```py
class Deployment:
    """
    Structure of the schema defining a deployment
    """

    # required defining data
    name: str 
    flow_id: UUID
    entrypoint: str
    path: str = None

    # workflow scheduling and parametrization
    parameters: Optional[Dict[str, Any]] = None
    parameter_openapi_schema: Optional[Dict[str, Any]] = None
    schedules: list[Schedule] = None
    paused: bool = False
    trigger: Trigger = None

    # metadata for bookkeeping
    version: str = None
    description: str = None
    tags: list = None

    # worker-specific fields
    work_pool_name: str = None
    work_queue_name: str = None
    infra_overrides: Optional[Dict[str, Any]] = None
    pull_steps: Optional[Dict[str, Any]] = None
```

Deployments are essentially defining metadata

#### Define and run prefect deployments

Deployments can be created like this. where `hello_world` is a flow

```py
hello_world.serve(name="my-first-deployment",
                      tags=["onboarding"],
                      parameters={"goodbye": True},# flow params
                      interval=60)
```
You can run the deployment like this

```py
from prefect.deployments import run_deployment
run_deployment(name="hello_world/my-first-deployment")
```

Or, you can run on the commandline

```shell
prefect deployment run 'hello_world/my-first-deployment'
```

### A minimal example

```python
from prefect import flow
from prefect import task

@task
def laugh():
	pass

@task
def run():
	pass

@task
def swim():
	pass

@task
def walk():
	pass

@flow
def first_subflow():
	laugh()
	run()

@flow
def second_subflow():
	laugh()
	run()

@flow
def pipeline():
    # do stuffs
    first_subflow()
    second_subflow()




if __name__ == "__main__":
    pipeline.serve(name="ml-pipeline")
```

Then on the shell we run

```shell
prefect deployment run 'pipeline/ml-pipeline'
```

It will produce something like this

```
Creating flow run for deployment 'pipeline/canon-pipeline'...
Created flow run 'beautiful-nyala'.
└── UUID: 45ef0da2-ff32-472e-a9b8-8fecdeb95b10
└── Parameters: {}
└── Job Variables: {}
└── Scheduled start time: 2024-07-03 19:20:02 +04 (now)
└── URL: http://path-to-server:4200/flow-runs/flow-run/45ef0da2-ff32-472e-a9b8-8fecdeb95b10
```

#### The prefect server

If you go to the prefect server you can see:

![Selection_383](https://github.com/pythonkitchen/pythonkitchen/assets/22630684/4ab235d6-6b54-48f0-b019-69cfbebe3cdb)
![Selection_382](https://github.com/pythonkitchen/pythonkitchen/assets/22630684/1c371598-feab-407d-a7ab-c17e31d7a8f5)

You can click on the toggle to activate then press the run button or select interval, which can also be defined when serving

### FAQ
**Q: What is the difference between a Flow and a Deployment?**
A: A Flow is the logic; a Deployment is the plan for *how* the flow should be executed (schedule, infrastructure, parameters).

**Q: Can I schedule a deployment via code?**
A: Yes, using the `.serve(..., cron="0 * * * *")` argument or via the UI.

**Q: Where do the logs go?**
A: Logs are captured by the Prefect server and can be viewed in the UI dashboard shown in the screenshots above.
