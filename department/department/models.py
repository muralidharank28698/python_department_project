from django.db import connections
from django.db import models
from django.db.models.fields import FilePathField
import os
import datetime
import base64

# def filepath(request, filename):
#     old_filename = filename
#     timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
#     filename = "%s%s" % (timeNow, old_filename)
#     return os.path.join('',filename)

class Register(models.Model):
    uname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    class Meta:
        db_table="register"




class Faculty(models.Model):
    name = models.CharField(max_length=100)
    
    # profile = models.ImageField(upload_to=FilePathField,null=True,blank=True)
    # profile = base64.decodestring(profile2)
    # print(profile)
    profile = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    class Meta:
        db_table="faculty"


