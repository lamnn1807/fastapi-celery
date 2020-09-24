# FastAPI with Celery

> Minimal example utilizing FastAPI and Celery with RabbitMQ for task queue, flower for monitoring the Celery tasks.

## Requirements

- Docker
  - [docker-compose](https://docs.docker.com/compose/install/)

## Run example

1. Run command ```docker-compose up```to start up the RabbitMQ, flower and our application/worker instances.
2. Navigate to the [http://localhost:8000/docs](http://localhost:8000/docs) and execute test API call. You can monitor the execution of the celery tasks in the console logs or navigate to the flower monitoring app at [http://localhost:5555](http://localhost:5555) (username: user, password: test).

## Run application/worker without Docker?

```python3 -m venv env```

```source ./env/bin/activate```

```pip install -r requirements.txt```

### Requirements/dependencies

- Python >= 3.7
- RabbitMQ instance

> The RabbitMQ, Redis and flower services can be started with ```docker-compose -f docker-compose.production.yml up```

### Install dependencies

Execute the following command: ```pip install -r requirements.txt```

### Run FastAPI app and Celery worker app

1. Start the FastAPI web application with ```uvicorn main:app --reload```.
2. Start the celery worker with command ```celery worker -A worker.celery_worker -l info -Q test-queue -c 1```
3. Navigate to the [http://localhost:8000/docs](http://localhost:8000/docs) and execute test API call. You can monitor the execution of the celery tasks in the console logs or navigate to the flower monitoring app at [http://localhost:5555](http://localhost:5555) (username: user, password: test).