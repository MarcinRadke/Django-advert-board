# Django advert table

Advert table site using Python, Django, Angular

## Installation

Prerequisites:

[Python](https://www.python.org/downloads/release/python-397/) 3.9.7 to install Django and its components.

[node js](https://nodejs.org/en/) 16.4.2 LTS

Create venv in your Django project folder:

```bash
python -m venv venv
```

## Django installation

Activate venv by typing 

```bash
.\venv\Scripts\activate
```

In venv download [Django](https://docs.djangoproject.com/en/4.0/intro/install/) 4.0.3, [djangorestframework](https://www.django-rest-framework.org/) 3.13.1, [django-cors-headers](https://pypi.org/project/django-cors-headers/) 3.11.0:

```bash
pip install Django
pip install djangorestframework
pip install markdown
pip install django-filter
pip install django-cors-headers
```

## Angular

Install [Angular](https://angular.io/) 13.3.2:

```bash
npm install -g @angular/cli
```

## Using Django and Angular

Run Django project in your venv by typing

```bash
python manage.py runserver
```

Server should be on site 127.0.0.1:8000

Angular is used with Django only on this port, else it might not work.

On main site there is list of other sites you can use to create, read, update, delete advertisments. You can also manage advertisments through admin site and Postman. To use admin site you must go to 127.0.0.1:8000/admin and use login: marci and password: django123 Password should be changed using command in venv:
```bash
python manage.py changepassword marci
```

Run angular server by using command in cmd in project folder:

```bash
ng serve --open
```
Angular server should be on site localhost:4200  

On Angular site you can read offers and its details. You can also filter through offers by using bars on top.
