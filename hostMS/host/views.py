from django.shortcuts import render

# Create your views here.

def index(req):
    req.user
    return render(req,'index.html')