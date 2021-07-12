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

### Django

- When you install Django, it also installs a command line toll called:
  - django-admin
- To create a project, type:
  - django-admin startproject <project name>

#### New Project files:

- `__init__`.py
  - This is a blank Python script that due to its special name let's Python know that this directory can be treated as a package
- settings.py
  - This is where we will store all our project settings
- urls.py
  - This is a Python script that will store all the URL patterns for our project. Basically the different pages of our web application
- wsgi.py
  - This is a Python script that acts as the Web Server Gateway Interface. It will later on help us deploy our web app to production
- manage.py
  - This is a Python script that we will use a lot. It will be associated with many commands as we build our web app
