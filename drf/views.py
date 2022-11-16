from django.shortcuts import render
from rest_framework.views import APIView
from todoapp.models import *
from rest_framework.response import Response
from .serializers import taskSerializers
from django.contrib.auth.decorators import login_required
# Create your views here.



# @login_required(login_url='/signin/')
class taskapi(APIView):
    def get(self,request):
        query = task.objects.all()
        serializer = taskSerializers(query, many=True)
        return Response(serializer.data)













