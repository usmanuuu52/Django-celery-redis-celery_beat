from django.http import JsonResponse
from .tasks import add  # Import the Celery task

def trigger_task(request):
    result = add.delay(4, 6)  # Trigger the Celery task
    return JsonResponse({'task_id': result.id})  # Return the task ID as a JSON response
