from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
userlist = []

def index(request):
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        userlist.append({"user":username,"password":password})

    # return HttpResponse('Hello world')
    return render(request,"index.html",{"data":userlist})