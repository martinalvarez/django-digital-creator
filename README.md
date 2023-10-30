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
    The funciton handler will return a HttpResponse object

### Create urls.py file in music app
 Add the urlpatterns list. Each element is a path element where you define the path and the view