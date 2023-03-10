from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@api_view(['GET','POST'])
def home(request):
    return Response({'msg':'hello user this is our plagarism'},status=status.HTTP_200_OK)