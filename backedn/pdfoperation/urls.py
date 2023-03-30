from django.urls import path,include
from .views import getreference,mergepdf,scannedpdf,extractimage
urlpatterns = [

    path('getreference/',getreference,name='getreference'),
    path('pdfmerge/',mergepdf,name='merge pdf'),
    path('scannedpdf/',scannedpdf,name='scan pdf'),
    path('extractimage/',extractimage,name='extractimage'),
    
    
    
    
    
]