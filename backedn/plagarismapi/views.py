from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from difflib import SequenceMatcher
# Create your views here.
@api_view(['GET','POST'])
def home(request):
    return Response({'msg':'hello user this is our plagarism'},status=status.HTTP_200_OK)

def wordplagariser(request):
    with open("page1.docx",'r', encoding='utf-8', errors='ignore') as file1 ,open("page2.docx",'r', encoding='utf-8', errors='ignore') as file2:
        filldata=file1.read()
        fill2data=file2.read()
        similarity=SequenceMatcher(None,filldata,fill2data).ratio()
        print(similarity*100)