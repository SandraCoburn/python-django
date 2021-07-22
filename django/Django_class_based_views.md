# Advanced Django

## Class Based Views "CBV"

- Django provides really powerful tools to use OOP and classes to define views
- The CBV offers great functionality and for most experienced users of Django, it is their default choic for creating views
- We will use the simplest available Django View Class:
  - from djangoviews.generic import View
  - We will also have to slightly change the way we call a class based view in the urls.py file of our project
  - We need to add in a .as_view() call off the class, this is an inherited method from the View
- We can also use the TemplateView that comes with Djangp
  Example:

```
#Function Based View
def index(request):
  return render(request, 'index.html')

#Class Based Template View
class IndexView(TemplateView):
  template_name = 'index.html
```

## CRUDE

- Create, Retrieve, Update and Delete
- Django has class based views to simplify this entire process
- CreateView class
- UpdateView class
- DeleteView class
