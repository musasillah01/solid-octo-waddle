'''
# Intro to Django
# django's documentation is a good read NOTED
# it has high affinity to relational databases. Object Relational Mapper (ORM)
# Model-view-controller (MVC) architecture is a patern that separates our app into 3 layers
# Model - contains all data related logic in an app.
# View - how the data is presented to the user
# Controller - an interface btw the model and view component

# Django is an MVT/MTV framework [T for template]

# View - concerns what data is presented to the user. Handles interaction btw the teemplate and the model.

# Template - concerned with how the data is presented to the user

# python installer packages [PIP]

# to start a new Django project ["django-admin startproject my_new_project"]

# no need to build an admin side bcos of the [content administration]

# to run our project we use the command (to start up our server) [python manage.py runserver]
# [
    __init__.py - tells python that the folder(django app) is a python package
    
    asgi.py - enables ASGI (Asynchronous functionalities) compatible web servers to serve the project (django 3 only)
    
    settings.py - settings for our django project anf every project must have this file
    
    urls.py = contains project level URL configurations,
    
    wsgi.py - enables WSGI compatible web servers to serve the project.
    
]
# [ use this command to create a django project [python manage.py startapp ourapp]
    
 we also need a urls.py file in our project
    
python manage.py migrate to make migrations

python manage.py createsuperuser
]
[
    # django-admin startproject fireflies
]
'''

'''
[learn with femi]
[
    it is possible to have/create multiple apps in a project
    
    to start an app use: "python manage.py startapp blog"
    
    map app view to app url or path
    then include the app url in the project directory example ('blog.url')
    
    after creating an app, register it in the settings under the list of installed apps
]

[
    do a repo and clone b4 building project
    
    git clone + link
    
    otherwise
    git init

    git remote add origin https://github.com/musasillah01/solid-octo-waddle.git
    
    git remote -v # shows remote dir project is connected to
    
    # b4 pushing we need to commit our project
    
    git status
    
    git pull origin main# name of repo/ placeholder
    
    git add .
    # we do git add . b4 commiting
    git commit -m "ready to be pushed to github" # describe what you are commiting
    
    git push origin main # to push
]

'''