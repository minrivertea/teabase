from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'^$', index, name="home"),
    url(r'^teas/$', teas, name="teas"),
    url(r'^teas/(\w+)/$', tea, name="tea"),
    url(r'^teas/(\w+)/(\w+)$', tea_instance, name="tea_instance"),
    url(r'^farms/$', farms, name="farms"),
    url(r'^farms/(\w+)/$', farm, name="farm"),

    url(r'^add_tea_type/$', add_tea_type, name="add_tea_type"),
    url(r'^add_farm/$', add_farm, name="add_farm"),

    url(r'^add_photo/(\w+)/$', add_photo, name="add_photo"),
    url(r'^add_instance/(\w+)/$', add_instance, name="add_instance"),
)
