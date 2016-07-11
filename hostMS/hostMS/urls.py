"""hostMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from host.views import *
# from django.core.management import execute_from_command_line
from host import urls as host_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', index,name='dashboard'),
    url(r'^',include(host_urls)),
    url(r'^$', hosts, name='hosts'),
    url(r'^assets/$', assets, name='assets'),
    url(r'^monitor/$', monitor, name='monitor'),
    url(r'^acc_login/$', acc_login, name='acc_login'),
]
