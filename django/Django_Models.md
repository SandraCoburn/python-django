# Django - Models

How to use Models and Databases

- We use Models to incorporate a database into a Django Project
- Django comes equipped with SQLite
- Django can connect to a variety of SQL engine backends
- In the settings.py file we can edit the `ENGINE` parameter used for `DATABASES`
- To create an actual model, we use a class structure inside of the relevant applications models.py file
- This class object will be a subclass of Django's built-in class:
  - django.db.models.Model
  - Each attribute of the class represents a field, which is just like a column name with constraints in SQL

## SQL Databases

- SQL operates like a giant table, with each column representing a field, and each row representing an entry
- Each column has a type of field, such as a CharField, IntegerField, DateField, etc
- Each field can also have constraints
  - For ex., a CharField should have a max_length constraint, indicating the maximum number of characters allowed
- Table(or models) relationships
- Often models will reference each other:

| WebsiteId | WebsiteName | URL              |
| --------- | ----------- | ---------------- |
| 1         | Google      | www.google.com   |
| 2         | Facebook    | www.facebook.com |

- For this referencing to work we use the concepts of Foreign Keys and Primary Keys

  - A primary key is a unique identifier for each row in a table
  - A foreign key just denotes that the column coincides with a primary key of another table

- Model classes:

```
class Topic(models.Model):
  top_name = models.CharField(max_length=264, unique=True)

class Webpage(models.Model):
  category = models.ForeignKey(Topic)
  name = models.CharField(max_length=264)
  url = models.URLField()

  def __str__(self):
    return self.name
```

- After we've set up the models we can migrate the database
- This basically let's Django do the heavy lifting of creating SQL databases that correspond to the models we created
- Django can do this entire process with a simple command:
  - python manage.py migrate
  - Then register the changes to your app, shown here with some generic "app1":
    - python manage.py makemigrations app1
  - Then migrate the database one more time:
    - python manage.py migrate
  - We can then later on use the shell from the manage.py file to play around with the models
    - python3 manage.py shell
  - In order to use the more convenient Admin interface with the models however, we need to register them to our application's admin.py file:
    ```
    from django.contrib import admin
    from app.models import Model!, Model2
    admin.site.register(Model1)
    admin.site.register(Model2)
    ```
- With the models and database created, we can use Django's Admin interface to interact with the database
- This Admin interface is one of the key features of Django
- To use the databese and the Admin , we will need to create a "superuser"
- We can do this with the following:
  - python manage.py createsuperuser
  - Providing a name, email, and password
- After setting up the models, we can populate them with some test data
- We will use Faker library
  - pip install Faker
