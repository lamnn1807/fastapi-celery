import os
from dotenv import load_dotenv, find_dotenv
from celery import Celery

load_dotenv(find_dotenv())

celery_app = None
celery_app = Celery(
    "worker", 
    broker=os.getenv("CELERY_BROKER"),
    backend=os.getenv("CELERY_BACKEND"),
)
celery_app.conf.task_routes = {
    "worker.celery_worker.test_celery": "test-queue"}

celery_app.conf.update(task_track_started=True)
