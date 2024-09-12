from celery import shared_task
from celery.exceptions import Ignore

@shared_task(bind=True, max_retries=3)
def add(self, x, y):
    try:
        # Task logic
        return x + y
    except Exception as exc:
        raise self.retry(exc=exc)
    
@shared_task
def print_message():
    return "Hello this is celery beat"
