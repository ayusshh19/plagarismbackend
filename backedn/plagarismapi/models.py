from django.db import models

# Create your models here.
class Studetails(models.Model):
    username=models.CharField(max_length=100)
    fullname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    rollno=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    
class Teacherdetails(models.Model):
    name=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
class Documents(models.Model):
    userid=models.ForeignKey(Studetails,on_delete=models.CASCADE)
    docname=models.FileField(upload_to='documents/')
    plagarism=models.FloatField(default=0.0)
    uploadtime=models.TimeField(auto_now_add=True)