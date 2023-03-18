from django.db import models
import os
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
    
def get_upload_path(instance, filename):
    return os.path.join('worddocument',instance.topic, filename)

class Documents(models.Model):
    userid=models.ForeignKey(Studetails,on_delete=models.CASCADE)
    docname=models.FileField(upload_to=get_upload_path)
    plagarism=models.FloatField(default=0.0)
    topic=models.CharField(default='chap1',max_length=100)
    uploadtime=models.TimeField(auto_now_add=True)
    
class pdfdoc(models.Model):
    userid=models.ForeignKey(Studetails,on_delete=models.CASCADE)
    pdfname=models.FileField(upload_to=get_upload_path)
    plagarism=models.FloatField(default=0.0)
    topic=models.CharField(default='chap1',max_length=100)
    uploadtime=models.TimeField(auto_now_add=True)
    
    