from django.urls import path,include
from .views import home,process_image,wordtotext,extract_text_from_pdf,imagefeature,handwritten,normalhandwritten
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home,name='Myhome'),
    path('imgtotext/',process_image,name='imagetotext'),
    path('wordtotext/',wordtotext,name='wordtotext'),
    path('pdftotext/',extract_text_from_pdf,name='extract_text_from_pdf'),
    path('imagefeature/',imagefeature,name='imagefeature'),
    path('handwritten/',handwritten,name='handwritten'),
    path('normal/',normalhandwritten,name='normal')
    
    
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)