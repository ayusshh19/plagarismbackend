from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from difflib import SequenceMatcher
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Documents
import os
from PIL import Image
from pathlib import Path
import pytesseract
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
@api_view(['GET','POST'])
def home(request):
    return Response({'msg':'hello user this is our plagarism'},status=status.HTTP_200_OK)

def wordplagariser(file1,file2):
    with open(file1,'r', encoding='utf-8', errors='ignore') as file1 ,open(file2,'r', encoding='utf-8', errors='ignore') as file2:
        filldata=file1.read()
        fill2data=file2.read()
        similarity=SequenceMatcher(None,filldata,fill2data).ratio()
        return similarity*100
        
MEDIA_ROOT=BASE_DIR/'media'  
   
def get_media_files(topic,type):
    media_files = []
    checkdir=False
    index=0
    currentno=0
    for root, dirs, files in os.walk(MEDIA_ROOT):
        # print(f'dirs {dirs}  files {files}')
        if topic in dirs:
            checkdir=True
            index=dirs.index(topic)
            # print(f'index {index}')
            
        if checkdir :
            if index==currentno:
                # print(f'media file length {len(media_files)}')
                for file in files:
                    media_files.append(os.path.join(root, file))
                if len(media_files)>1:
                    checkdir=False
                    currentno+=1
               
        
    return media_files

@receiver(post_save, sender=Documents)
def do_something(sender, instance, **kwargs):
    scoreindex=[]
    if instance.docname:
        File_List=get_media_files(instance.topic,'worddocument')
        setfile=str(instance.docname).split('/')
        setfilenew="\\".join(setfile)
        print(setfilenew)
        filename=os.path.join(MEDIA_ROOT, str(setfilenew))
        for item in File_List:
            print(f'item {item} filename {filename} is equeal {item==filename}')
            if item == filename:
                scoreindex.append(0)
                continue
            else:
                result=wordplagariser(filename,item)
                scoreindex.append(result)
        try:
          if len(scoreindex)>0:
              print(Documents.objects.filter(id=instance.id))
              success=Documents.objects.filter(id=instance.id).update(plagarism=max(scoreindex))
              print(success)
              print(scoreindex)
              print(f'success {success}')
        except :
          print('An exception occurred')
          
@api_view(['GET','POST'])
def process_image(request):
    if request.method == 'POST':
        print(request.data)
        images = request.FILES.getlist('images')
        imagetextlist=[]
        for image in images:
            image = Image.open(image)
            text = pytesseract.image_to_string(image)
            imagetextlist.append(text)
        similarity=SequenceMatcher(None,imagetextlist[0],imagetextlist[1]).ratio()
        return Response({'msg':'my post request','Score':similarity*100},status=status.HTTP_200_OK)
    return Response({'msg':'get request'},status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def wordtotext(request):
    if request.method == 'POST':
        print(request.data)
        worddoc = request.FILES.getlist('worddocuments')
        wordlist=[]
        for word in worddoc:
            image = Image.open(image)
            text = pytesseract.image_to_string(image)
            wordlist.append(text)
        similarity=SequenceMatcher(None,wordlist[0],wordlist[1]).ratio()
        return Response({'msg':'my post request','Score':similarity*100},status=status.HTTP_200_OK)
    return Response({'msg':'get request'},status=status.HTTP_200_OK)
