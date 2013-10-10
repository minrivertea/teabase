from django import forms
from django.conf import settings
from django.forms import ModelForm
from django.contrib.auth.models import User


from models import *

 
class TeaAddForm(ModelForm): 
    class Meta:
        model = Tea
        # exclude = ('owner', 'is_preferred',)
        
        
class TeaInstanceAddForm(ModelForm): 
    class Meta:
        model = TeaInstance
        # exclude = ('owner', 'is_preferred',)
        
        
class PhotoAddForm(ModelForm): 
    class Meta:
        model = Photo
        exclude = ('date_uploaded', 'tea_instance')


        
class FarmAddForm(ModelForm): 
    class Meta:
        model = Farm
        # exclude = ('owner', 'is_preferred',)