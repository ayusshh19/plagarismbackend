from django.contrib import admin
from .models import Studetails,Teacherdetails,Documents
# Register your models here.

@admin.register(Studetails)
class StudetailsAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Studetails._meta.fields]

    
# Register your models here.
@admin.register(Teacherdetails)
class Teacherdetailsadmin(admin.ModelAdmin):
    list_display=[f.name for f in Teacherdetails._meta.fields]

# Register your models here.
@admin.register(Documents)
class cartitemadmin(admin.ModelAdmin):
    list_display=[f.name for f in Documents._meta.fields]