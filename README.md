![Bitbucket Pipelines](https://img.shields.io/bitbucket/pipelines/paulrogers/django-mailer/master)
[![Python Version](https://img.shields.io/badge/python-3.10-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-4.2-brightgreen.svg)](https://djangoproject.com)

# Django Mailer with DRF

Run your app in a Virtual Environment: http://python-guide-ru.readthedocs.io/en/latest/dev/virtualenvs.html

Install the requirements:
```shell
pip install -r requirements.txt
```

Run the development server:
```shell
python manage.py runserver
```

Run Celery:
```shell
celery -A project.celery worker -l info
```

Test email:
```shell
from django.core.mail import send_mail

send_mail('Testing', 'Testing message, can you hear me...', 'your-email@mail.com', ['test@gmail.com', 'test@mail.com'])
```
