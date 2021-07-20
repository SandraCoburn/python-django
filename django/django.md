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
  path('first_app/', include('first_app.urls')),
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

## Templates

- The template will contain the static parts of an html page(parts that are always the same)
- Template tags have their own special syntax
- This syntax allows us to inject dynamic contento that our Django App's views will produce, effecting the final HTML
- First create a templates directory and then a subdirectory for each specific app's template
- It goes inside of your top level directory:
  - first_project/templates/first_app
- Next step is to let Django know of the templates by editing the DIR key inside of the TEMPLATES dictionary in the settings.py file
- Python's os module dynamically generate the correct file path strings, regardless of computer
- Import os and try the following:

```
print(__file__)
print(os.path.dirname(__file__))
```

- We will use this os module to feed the path to the DIR key inside of the TEMPLATES dictionary
- Once we've done that we can create an html file called index.html inside of the templates/first_app directory
- Inside this HTML file we will instert template tags(a.k.a Django Template Variables)
- These template variables will allow us to inject content into the HTML directly from Django

### Dynamic paths

- Open first_project/settings.py
- Create a new folder in first_project named templates
- Add template path to settings

```
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = Path(BASE_DIR)/'templates'
print("temp direc",TEMPLATES_DIR)
```

### Static Files

- Create a new directory inside of the project called static
- Add this directory path to the project;'s settings.py file
- Add a STATIC_URL variable
- Create a directory inside of static called images to store static image files
- To check: 127.0.0.1:800/static/images/pict.jpg
- Add a template tag:
  - Inside html file, we add in a few specific tags, at the top:
    - {% load staticfiles %}
  - Then insert the image with an HTML `<img src=""> `style tag using:
    - `<img src={%static "images/pic.jpg" %}>`

### More About Templates

- We can use templates to have a "base" template and inherit that template in the .html files
- Templates are also used to solve issues with relatives paths and working with variables
- Templates can also help solve issues by avoiding hard-coded URL paths
- Templates come with built-in filter capabilities so you can adjust variables on the actual individual page

#### Templates for Relative URLs

- IF we want our Django project to work on any system, It is a poor practice to use an anchor tag with an href we've passed in a harcoded path to the file
- How can we replace a hardcoded URL path in an href with a URL Template?

  - 1. With the use of URLs in our templates. For example:

  ```
  <a href="basicapp/thankyou>Thanks</a>
  #Can be changed to:
  <a href="{% url "thankyou%}>Thanks</a>

  #name='thankyou' is in the urls.py file
  ```

  - 2. Could also just directly reference the view. For example:

  ```
  <a href="basicapp/thankyou>Thanks</a>
  #Can be changed to:
  <a href="{% url'basicapp.iews.thankyou'%}">Thanks</a>
  ```

  - The suggested (and most future-proof) method to do all of this involves the urls.py file
  - Inside the urls.py file we add in the variable app_name
  - We then set this variable equal to a string that is the same as your app name

  ```
  <a href="basicapp/thankyou>Thanks</a>
  #Can be changed to:
  <a href="{% url'basicapp:thankyou'%}">Thanks</a>
  ```

  - This method requires that app_name variable to be created inside the urls.py file

#### Django Template Inheritance

- Template inheritance allows us to create a base template we can inherit from
- This idea is sometimes also known as template extending, as in extending the base.html to other html files
- The inheritance doesn't need to just be limited to one base.html file, you can extend multiple templates
- Main steps for inheritance:
  - Find repetitive parts of your project
  - Create a base template of them
  - Set the tags in the base template
  - Extend and call those tags anywhere
    Example `base.html`:

```
<link to JS, CSS, Bootstrap>
<bunch of html like navbars>
  <body>
  {% block body_block%}
  {%  endblock%}
  </body>
</More footer html>
```

Example `other.html`:

```
<!DOCTYPE html>
{% extends "basic_app/base.html"%}
{% block body_block %}
<HTML specific fo other.html>
<HTML specific for other.html>
{% endblock %}
```

#### Template Features, Filters and Custom Filters

- Django provides a ton of easy to implement template filters that allow us to effect the injection of customized code to edit information in various views/pages before displaying it to the user
- The general form for a template filter is:
  - {{ value | filter: 'paramenter'}}
  - Not all filters take in parameters
  - Many of these filters are based off of common built-in Python functions
- [documentation](https://docs.djangoproject.com/en/3.2/ref/templates/language/) for Django Templates
