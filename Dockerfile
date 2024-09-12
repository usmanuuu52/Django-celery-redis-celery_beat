# Dockerfile

# Base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Expose port 8000 for Django
EXPOSE 8000

# Run Django server, Celery worker, and Celery beat scheduler
CMD ["sh", "-c", "python manage.py migrate && \
                  celery -A myproject worker --loglevel=info & \
                  celery -A myproject beat --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler & \
                  python manage.py runserver 0.0.0.0:8000"]
