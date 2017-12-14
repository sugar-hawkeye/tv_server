from django.shortcuts import render
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import  check_password

from .models import Client,ClientAuth
from .serializers import ClientAuthSerializer

class ClientAuthView(APIView):
    def post(self, request, format=None):
        serializer = ClientAuthSerializer(data=request.data)
        if serializer.is_valid():
            if request.data['identity_type'] == 'P':
                obj = serializer.save()
                if obj:
                    phone = request.data['identifier']
                    Client(phone=phone,client_id=obj,nickname=phone).save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ClientLogin(APIView):
    def post(self, request, format=None):
        username = request.data['identifier']
        key = request.data['credential']
        obj = ClientAuth.objects.get(identifier=username)
        if obj:
            if check_password(key,obj.credential):
                t = model_to_dict(obj)
                result = {'result':'ok',"data":t}
                return Response(result, status=status.HTTP_201_CREATED)
        result = {'result': 'faile'}
        return Response(result, status=status.HTTP_400_BAD_REQUEST)