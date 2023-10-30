# django-digital-creator
django project

## Steps

### Clone the empty repository
    git clone https://github.com/martinalvarez/django-digital-creator.git

### Install virtual environment
    python -m venv myenv

### Active the virtual environment
    source myenv/bin/activate

### Install Django
    pip install Django

### Create the core application
    python django-admin core .

### Run the server to test that everything is working properly
    python manage.py runserver

## Create a new app called music
    python manage.py startapp music

## Add the new app in core/settings.py
Add the 'music' element in INSTALLED_APPS list.

### Create a view in music app
The function handler will return a HttpResponse object

### Create urls.py file in music app
Add the urlpatterns list. Each element is a path element where you define the path and the view

### Create templates folder
Add html files and use render function passing the request and the html name file. You can send a context object to use it and show dynamic content

### Models
Add your models that will be mapped with tables in the DB.

### After creating/updating models, run:
    python manage.py makemigrations
    
### After creating the migrations files apply them running:
    python manage.py migrate

### You can create an empty migration to execute sql statements
    python manage.py makemigrations music --empty    
