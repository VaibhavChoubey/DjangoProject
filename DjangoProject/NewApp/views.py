from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def WelcomePageView(request):
    return HttpResponse("Welcome to homepage")

def UserName (request):
    return render(request , "Username.html" , context={"Name":"Vaibhav"})