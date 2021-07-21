from django.shortcuts import render
from .forms import UserProfileInfoForm, UserForm

#Extra import for the Login and Logout capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
  return render(request, 'basic_app/index.html')

@login_required
def user_logout(request):
  logout(request)
  return HttpResponseRedirect(reverse('index'))

def register(request):
  # assumed at first user is not registerd so we set it to false
  registered = False

  # check the request and set registered to true if everything is right and user could gets registered
  if request.method == "POST":
    user_form = UserForm(data=request.POST)
    profile_form = UserProfileInfoForm(data=request.POST)

    if user_form.is_valid() and profile_form.is_valid():

      user = user_form.save()
      user.set_password(user.password)
      user.save()

      profile = profile_form.save(commit=False)
      # define one to one relationship
      profile.user = user

      #Check if there is a profile picture
      if 'profile_pic' in request.FILES:
        profile.profile_pic = request.FILES['profile_pic']
      
      profile.save()

      registered = True
    else: 
      print(user_form.errors, profile_form.errors)
#If there was no request == to post, we set up the forms
  else: 
    user_form = UserForm()
    profile_form = UserProfileInfoForm()
  return render(request, 'basic_app/registration.html',{'user_form':user_form, 'profile_form':profile_form, 'registered':registered})

def user_login(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username,password=password)

    if user:
      if user.is_active:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
      else:
        return HttpResponse("Account not active")
    else:
      print("Someone tried to login and failed")
      print("Username: {} and password {}".format(username,password))
      return HttpResponse("Invalid login details supplied!")
  else:
    return render(request, 'basic_app/login.html')