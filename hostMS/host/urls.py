from django.conf.urls import include, url
from  host import views

urlpatterns = [
    url(r'^host_mgr/$', views.host_mgr,name='host_mgr'),
]