from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from models import *
# Create your views here.

def index(req):
    return render(req,'index.html')

def hosts(req):
    return render(req,'hosts.html')

def assets(req):
    return render(req,'assets.html')

def monitor(req):
    return render(req,'monitor.html')

def acc_login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        print request.POST
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            return render(request,'login.html',{'log_err':"Wrong username or password!"})

# def host_mgr(request):
#     select_group_id = request.GET.get("selected_group")
#     if select_group_id:
#         host_list = BindHostToUser.objects.filter(host_groups__id=select_group_id)
#     else:
#         host_list = request.user.bind_hosts.select_related()
#     return render(request,'hosts/host_mgr.html',{'active_main_node':'/hosts/','host_list':host_list})

def host_mgr(req):
    return render(req,'hosts.html',locals())