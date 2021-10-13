from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class post_sign(APIView):
    @csrf_exempt
           
    def post(self,request):
        try:
            
            request_data=request.data
            print(request_data)
        
            username=request_data['data']['username']
            email=request_data['data']['email']
            password=request_data['data']['password']
            first_name=request_data['data']['first_name']
            last_name=request_data['data']['last_name']
            confirm_password=request_data['data']['confirm_password']
            print(username)
            print(email)
            print(password)
            print(first_name)
            print(last_name)
            print(confirm_password)
            
            u=User.objects.get(username=username)
            if u:
                return Response(status =status.HTTP_400_BAD_REQUEST, data={"remarks": 'User Created already'})
            u1=User.objects.get(email=email):
            if u1:
                return Response(status =status.HTTP_400_BAD_REQUEST, data={"remarks": 'Email Created already'})
            if(password==confirm_password):
                user = User.objects.create_user(username,email,password)
                user.first_name=first_name
                user.last_name=last_name
                user.save()
                return Response(status=status.HTTP_200_OK, data={"remarks":'User Created Successfully'})
            else:
                return Response(status =status.HTTP_400_BAD_REQUEST, data={"remarks": 'Password and Confirm Password do not match'})
        except :
            print("Error")
            
            
            
        
        
            
        
class post_login(APIView):
    @csrf_exempt
    def post_login(request):
        '''try:'''
        return Response(request.data )
        '''except:
            print("Error")'''
        
        
# Create your views here.
'''
@csrf_exempt
def post_login(request):
    request_json=json.loads(request.body)
    print (request_json)
    print(request_json['data']['username'])
    print(request_json['data']['email'])
    print(request_json['data']['password'])
    print(request_json['data']['first_name'])
    print(request_json['data']['last_name'])
    username=request_json['data']['username']
    email=request_json['data']['email']
    password=request_json['data']['password']
    first_name=request_json['data']['first_name']
    last_name=request_json['data']['last_name']
    print(username)
    print(email)
    print(password)
    print(first_name)
    print(last_name)
    user = User.objects.create_user(username,email,password)
    user.first_name=first_name
    user.last_name=last_name
    user.save()
    
    return JsonResponse(data=request_json, status=200)
    
    

def get_login(request):
    return HttpResponse("Details")
'''


