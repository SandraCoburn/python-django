from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.
def index(request):
  return HttpResponse("<em>My Second App</em> ")

def users(request):

  user_list = User.objects.order_by('first_name')
  user_dict = {'users': user_list}
  return render(request, 'appTwo/users.html', context=user_dict)

def help(request):
  help_dict = {'help_insert':'HELP PAGE'}
  return render(request, 'appTwo/help.html', context=help_dict)
