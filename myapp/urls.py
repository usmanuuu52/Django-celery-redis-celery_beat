from django.urls import path
from . import views  # Import views

urlpatterns = [
    path('', views.trigger_task),  # Correctly reference the view
]
