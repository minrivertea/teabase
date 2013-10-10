from django.db import models
from datetime import datetime


class Tea(models.Model):
    english_name = models.CharField(max_length=200)
    pinyin_name = models.CharField(max_length=200, blank=True, null=True)
    chinese_name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.english_name


class TeaInstance(models.Model):
    tea = models.ForeignKey(Tea)
    notes = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    date_picked = models.DateField(blank=True, null=True)
    date_tasted = models.DateField(blank=True, null=True)
    farm = models.ForeignKey('Farm', blank=True, null=True)
    
    def __unicode__(self):
        return self.tea
    
    def get_photos(self):
        return Photo.objects.filter(tea_instance=self)
    
    
class Photo(models.Model):
    image = models.ImageField(upload_to='tea_photos/')
    tea_instance = models.ForeignKey('TeaInstance')
    date_uploaded = models.DateTimeField(default=datetime.now())
    

class Farm(models.Model):
    english_name = models.CharField(max_length=200)
    pinyin_name = models.CharField(max_length=200, blank=True, null=True)
    chinese_name = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.english_name
    