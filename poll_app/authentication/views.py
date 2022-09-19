
import json

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from django.http import httpresponse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from authentication.models import Polls, UsersDetails
from django.core import serializers
from datetime import datetime, timedelta
from django.db.models.functions import Now



@csrf_exempt
def signup(request):
    request_data = json.loads(request.body)
    myuser = UsersDetails()
    myuser.username = request_data['username']
    myuser.fname = request_data['fname']
    myuser.lname = request_data['lname']
    myuser.email = request_data['email']
    myuser.pass1 = request_data['pass1']
    myuser.pass2 = request_data['pass2']
    check_existed_email = UsersDetails.objects.filter(
        email=request_data['email']).first()
    if check_existed_email:
        return_object = {
            "message": "Email Already existed, please try with diff email"
        }
        return JsonResponse(return_object, status=400)
    else:
        myuser.save()
        return_object = {
            "message": "Registration Successfull"
        }
        
        return JsonResponse(return_object, status=200)


@csrf_exempt
def login(request):
    request_data = json.loads(request.body)
    check_existed_username = UsersDetails.objects.filter(username=request_data['username'],pass1=request_data['pass1']).first()
    if check_existed_username:
        return_object = {
            "message": "login Successfully"
        }

        return JsonResponse(return_object, status=200)
    else:

        return_object = {
            "message": "invalid cred"
        }
        return JsonResponse(return_object, status=400)


@csrf_exempt
def create_poll(request):
    request_data = json.loads(request.body)
    existed_poll_by_user = Polls.objects.filter(email=request_data['email']).count()
    
    if existed_poll_by_user <5:
        poll= Polls()
        poll.email=request_data['email']
        poll.question=request_data['question']
        poll.opt1=request_data['opt1']
        poll.opt2=request_data['opt2']
        poll.opt3=request_data['opt3']
        poll.opt4=request_data['opt4']
        poll.save()
        return_object = {
            "message": "polls created Successfull"
        }
        
        return JsonResponse(return_object, status=200)
    else:
        return_object={
            "message":"cannot create this poll as you have alreay created the 5 polls"
        }
        return JsonResponse(return_object, status=400)


@csrf_exempt
def get_polls_by_user(request):
    request_data=json.loads(request.body)
    polls= Polls.objects.filter(email=request_data['email'])
    data = serializers.serialize('json',polls)
    return_object = {
        "message": "get polls data created by you successfully.",
        "result":json.loads(data)
    }
    
    return JsonResponse(return_object, status=200)


@csrf_exempt
def get_polls_created_by_others(request):
    request_data=json.loads(request.body)
    polls= Polls.objects.exclude(email=request_data['email'])
    data = serializers.serialize('json',polls)
    return_object = {
        "message": "get polls data created by others successfully.",
        "result":json.loads(data)
    }
    
    return JsonResponse(return_object, status=200)

@csrf_exempt
def get_profile_data(request):
    request_data=json.loads(request.body)
    polls= UsersDetails.objects.filter(email=request_data['email'])
    data = serializers.serialize('json',polls)
    return_object = {
        "message": " data fetch successfully.",
        "result":json.loads(data)
    }
    
    return JsonResponse(return_object, status=200)

@csrf_exempt
def data_24(request):
    Polls.objects.filter(created_on_date__lt=datetime.now() - timedelta(hours=24)).delete()
    return_object = {
            "message": "data deleted Successfull."
        }
    return JsonResponse(return_object, status=200)




    
    
    

       
    
    
