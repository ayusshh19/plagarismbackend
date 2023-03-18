from django.urls import path,include
from .views import home,process_image,wordtotext
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home,name='Myhome'),
    path('imgtotext/',process_image,name='imagetotext'),
    path('wordtotext/',wordtotext,name='wordtotext'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)