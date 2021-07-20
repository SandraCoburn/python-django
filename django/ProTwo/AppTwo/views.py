from django.shortcuts import render
# from django.http import HttpResponse
# from AppTwo.models import User
from AppTwo.forms import newUserForm

# Create your views here.
def index(request):
  return render(request, "appTwo/index.html")

def users(request):
  form = newUserForm()

  if request.method == "POST":
    form = newUserForm(request.POST)
    if form.is_valid():
      form.save(commit=True)
      return index(request)
    else: 
      print("ERROR from invalid")
  return render(request,"appTwo/users.html", {'form':form})


  # user_list = User.objects.order_by('first_name')
  # user_dict = {'users': user_list}
  # return render(request, 'appTwo/users.html', context=user_dict)

# def help(request):
#   help_dict = {'help_insert':'HELP PAGE'}
#   return render(request, 'appTwo/help.html', context=help_dict)
