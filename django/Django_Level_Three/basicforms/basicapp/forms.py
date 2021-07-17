from django import forms
#Built in validator
from django.core import validators

#custom validator
def check_for_z(value):
  if value[0].lower() != "z":
    raise forms.ValidationError("Name needs to start with Z")

class FormName(forms.Form):
  name = forms.CharField(validators=[check_for_z])
  email = forms.EmailField()
  verify_email = forms.EmailField(label='Enter your email again')
  text = forms.CharField(widget=forms.Textarea)

  def clean(self):
    all_clean_data = super().clean()
    email = all_clean_data['email']
    vmail = all_clean_data['verify_email']

    if email != vmail:
      raise forms.ValidationError("Make sure emails match")

  #hidden fields with buuilt in validator
  botcatcher = forms.CharField(required=False,widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
'''
ex of a validator without built in Django library:
def clean_botcatcher(self):
    botcatcher = self.cleaned_data['botcatcher']

    if len(botcatcher) > 0:
      raise forms.ValidationError("Gotcha Bot!")
    return botcatcher
'''
  