# Advanced Django

## Class Based Views "CBV"

- Django provides really powerful tools to use OOP and classes to define views
- The CBV offers great functionality and for most experienced users of Django, it is their default choic for creating views
- We will use the simplest available Django View Class:
  - from djangoviews.generic import View
  - We will also have to slightly change the way we call a class based view in the urls.py file of our project
  - We need to add in a .as_view() call off the class, this is an inherited method from the View
