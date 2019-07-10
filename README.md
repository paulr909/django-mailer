[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.2.2-brightgreen.svg)](https://djangoproject.com)

# Django Mailer with DRF

## Django 2.2.2

Run your app in a Virtual Environment: http://python-guide-ru.readthedocs.io/en/latest/dev/virtualenvs.html

Install the requirements:

```bash
pip install -r requirements.txt
```

Run the development server:

```bash
python manage.py runserver
```

Run Celery:

```bash
celery worker -A project.celery -l info
```

Test email:

```bash
from django.core.mail import send_mail

send_mail('Testing', 'Testing message, can you hear me...', 'your-email@mail.com', ['test@gmail.com', 'test@mail.com'])
`
