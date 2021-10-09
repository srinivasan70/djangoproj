from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json

# Create your views here.

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
