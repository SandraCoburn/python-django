# Django

### Virtual Environment

- A virtual environment allows you to have a virtual installation of Python and packages on your computer.
  - Packages change and get updated often!
  - There are changes that break backwards compatibility
- You crate a virtual environment that contains the newer version of the package.
- Anaconda makes this easy. A virtual environment handles is included
- To use a virtual environment with conda we use these commands:
  - conda create --name myEnv django
    - Here we created an environment called "myEnv" with the latest version of Django
  - You can then activate the environment:
    - activate myEnv
    - Now, anything installed with pip or conda when this environment is activated, will only be installed for this environment
  - You can deactivate the environment
    - deactivate myEnv

### Conda commands

- conda create --name myDjangoEnv django
- conda create --name myDjangoEnv python=3.5 #to specify python version
- conda activate myDjangoEnv
- conda install django #to install django in the virtual env
- conda deactivate #To get out of virtual env

### Django Project

- A `Django Project` is a collection of applications and configurations that when combined together will make up the full web application (your complete website running with Django)
- A `Django Application` is created to perform a particular functionality for our entire web application. For ex, we could have a registration app, a polling app, comments app, etc.
  - These Django Apps can then be plugged into other Django Projects, so we can reuse them.
- When you install Django, it also installs a command line toll called:
  - django-admin
- To create a `project`, type:
  - django-admin startproject <project name>
- Cd into project. To run server, type:
  - python3 manage.py runserver
- To create a new `app`:
  - python3 manage.py startapp first_app
- Go to first_project folder, open `settings.py`
  - Add new app to INSTALLED_APPS list
  - Run server again to be sure there is no errors
- Create a new `view`:

  - Go into first_app folder and open `views.py`

  ```
  from django.http import HttpResponse

  def index(request):
    return HttpResponse("Hello World!")
  ```

- Map the `view' to the URL.py file
  - Go to first_project folder and open urls.py to add views

```
  from first_app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
]
```

#### Using the include() function from django.conf.urls

- The include() function allows us to look for a match with regular expressions and link back to our application's own urls.py file
- We will have to manually add in this urls.py file
- We add the following to the project's urls.py

```
from django.conf.urls import include
ulrpatters = [...
  url(r'^first_app/', include('first_app.urls')),
...]
```

- This would allow us to look for any url that has the pattern: www.domainname.com/first_app/...
- If we match that pattern, the include() function basically tells Django to go look at the urls.py file inside of first_app folder

#### New Project files:

- `__init__.py`
  - This is a blank Python script that due to its special name let's Python know that this directory can be treated as a package
- `settings.py`
  - This is where we will store all our project settings
- `urls.py`
  - This is a Python script that will store all the URL patterns for our project. Basically the different pages of our web application
- `wsgi.py`
  - This is a Python script that acts as the Web Server Gateway Interface. It will later on help us deploy our web app to production
- `manage.py`
  - This is a Python script that we will use a lot. It will be associated with many commands as we build our web app

#### New App files:

- `__init__.py`
  - This is a blank Python script that due to its special name let's Python know that this directory can be treated as a package
- `admin.py`
- We can register our models here which Django will then use them with Django's admin interface.
- `app.py`
  - Here we can place application specific configurations
- `models.py`
  - Here we store the application's data models
- `tests1
  - Here we can store test functions to test our code
- `views.py`
  - This is where we have functions that handle requests and return responses
- `Migrations folder`
  - This directory stores database specific information as it relates to the models
