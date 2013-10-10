from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, Http404
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404

from PIL import Image
from cStringIO import StringIO
import os, md5
import smtplib
import re


# SITE
from utils import _render

# APP
from forms import *



def index(request):    
    return _render(request, 'home.html', locals())
    
def search(request):
    
    return _render(request, 'home.html', locals())
    
def teas(request):  
    teas = Tea.objects.all()  
    return _render(request, 'teas.html', locals())

def tea(request, id):
    tea = get_object_or_404(Tea, pk=id)
    tea_instances = TeaInstance.objects.filter(tea=tea)
    return _render(request, 'tea.html', locals())

def tea_instance(request, tea_id, id):

    tea_instance = get_object_or_404(TeaInstance, pk=id)

    return _render(request, 'tea_instance.html', locals())

def farms(request):
    farms = Farm.objects.all()    
    return _render(request, 'farms.html', locals())

def farm(request, id):
    farm = get_object_or_404(Farm, pk=id)
    return _render(request, 'farm.html', locals())

def add_farm(request):

    if request.method == 'POST':
        form = FarmAddForm(request.POST)
        if form.is_valid():
            instances = form.save()
            return HttpResponseRedirect(reverse('farm', args=[instances.id]))
    else:
        form = FarmAddForm()
    
    return _render(request, 'add_farm.html', locals())

def add_instance(request, id):

    tea = get_object_or_404(Tea, pk=id)
    if request.method == 'POST':
        form = TeaInstanceAddForm(request.POST)
        if form.is_valid():
            
            instances = form.save()

            return HttpResponseRedirect(reverse('tea', args=[tea.id]))
    else:
        form = TeaInstanceAddForm()

    return _render(request, 'add_tea_instance.html', locals())

def add_photo(request, tea_instance_id):
    
    tea_instance = get_object_or_404(TeaInstance, id=tea_instance_id)
    
    if request.method == 'POST':
        form = PhotoAddForm(request.POST, request.FILES)
        if form.is_valid():
            
            # add the photo and then save the model
            photo = request.FILES['image']
            image_content = photo.read()
            image = Image.open(StringIO(image_content))
            format = image.format
            format = format.lower().replace('jpeg', 'jpg')
            filename = md5.new(image_content).hexdigest() + '.' + format
            # Save the image
            path = os.path.join(settings.MEDIA_ROOT, 'tea_photos', filename)
            # check that the dir of the path exists
            dirname = os.path.dirname(path)
            if not os.path.isdir(dirname):
                try:
                    os.mkdir(dirname)
                except IOError:
                    raise IOError, "Unable to create the directory %s" % dirname
            open(path, 'w').write(image_content)
            
            thing = Photo.objects.create(
                image = "".join(('tea_photos/', filename)),
                date_uploaded = datetime.now(),
                tea_instance = tea_instance,
            )   
            
            print thing.image         

            return HttpResponseRedirect(reverse('tea_instance', args=[tea_instance.tea.id, tea_instance.id]))
    else:
        form = PhotoAddForm()
    
    return _render(request, 'add_photo.html', locals())
    

def add_tea_type(request):
    
    if request.method == 'POST':
        form = TeaAddForm(request.POST)
        if form.is_valid():             
            
            instances = form.save()
            return HttpResponseRedirect(reverse('tea', args=[instances.id]))
    else:
        form = TeaAddForm()
    
    return _render(request, 'add_tea_type.html', locals())