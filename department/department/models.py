from django.db import models

class Register(models.Model):
    uname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    class Meta:
        db_table="register"

