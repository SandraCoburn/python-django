from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

# Create your views here.
'''
#sample easy class based view
class CBView(View):
  def get(self, request):
    return HttpResponse('Class Based Views are Cool!')
'''

#Using Django TemplateView
class IndexView(TemplateView):
  template_name = 'index.html'

  #Injecting tags
  def get_context_data(self,**kwargs):
    context = super().get_context_data(**kwargs)
    context['injectme'] = "BASIC INJECTION"
    return context