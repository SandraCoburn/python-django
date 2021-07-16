# Django Forms

- Django Forms Advantages:
  - Quickly geneerate HTML form widgets
  - Validate data and process it into a Python data structure
  - Create form versions of our Models, quickly update models from Forms

## Create a Form

- Create a forms.py file inside the application
- Call Django's built in forms classes (looks very similar to creating models)
  Example:

```
from django import forms

class FormName(forms.Form):
  name = forms.CharField()
  email = forms.EmailField()
  text = forms.CharField(widget=forms.Textarea)
```

- Next we need to show it by using a view
  - Inside our views.py file we need to import the forms:
    - from . import forms or from forms import FormName # The . just indicates to import from the same directory as the current .py file
    - Create a new view for the form
    ```
    def form_name_view(request):
      form = forms.FormName()
      return render(request, "form_name.html", {'form':form})
    ```
    - Add the view to the app's urls, either directly or with include()
      - Directly:
      ```
      from basicapp import views
      urlpatterns = [
        ulr('formpage/', views.form_name_view, name='form_name')
      ]
      ```
      - Create the templates folder along with the html file that will hold the template tagging for the form
      - Update the settings.py file to reflect the TEMPLATE_DIR variable
      - Our views should reflect subdirectories inside templates
      - Go into the form_name.html file inside templates/basicapp and add in the actual template tagging that will create the Django form
      - "Inject" the form using template taging. You can pass in the key from the context dictionary:
        - {{form}}

### HTTP GET POST

- HTTP stands for Hypertext Transfer Protocol and is designed to enable communication between a client and a server.
  - The client submits a request, the server then responds
  - GET - requests data from a resource
  - POST - submits data to be process to a resource
- Site Security Measures

  - This is a Cross-Site Request Forgery (CSRF) token, which secures the HTTP POST action that is initiated on the subsequent submission of a form
  - The Django framework requires the CSRF token to be present
  - If it is not there, your fomr may not work
  - It works by using a 'hidden input' which is a random coce and checking that it matches the user's local site page
  - Add {% csrf_token%}
    ex.

  ```
  <div class ="container>
    <form method="POST">
      {{ form.as_p}}
      {% csrf_token %}
      <input type="submit" class="btn btn-primary" value="Submit">
    </form>
  </div>
  ```

  - Inform the view that if we get a POST back, we should check if the data is valid and if so, grab that data
  - We can do this by editing the view
  - Upon receiving a validated form, we can access a dictionary like attribute of the "cleaned_data"
    ex.

  ```
  def form_name_view(request):
    form = forms.FormName()

    #Check to see if we get a POST back
    if request.method == "POST":
      #In which case we pass in that request
      form = forms.FormName(request.POST)

      #Check to see form is valid
      if form.is_valid():
        #Do something
        print("Form Validation Success. Prin in console.")
        print("Name" + form.cleaned_data['name'])
        print("Email" + form.cleaned_data['email'])
        print("Text"+form.cleaned_data["text"])
    return render(request, "basicapp/form_page.html",{'form':form})
  ```