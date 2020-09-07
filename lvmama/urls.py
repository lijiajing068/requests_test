"""lvmama URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sign import views_if
from sign import views
from sign import xiews_if_sec
from django.conf.urls import url,include
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.index),
    path('index/', views.index),
    path('login_action/', views.login_action),
    path('event_manage/', views.event_manage),
    path('accounts/login/', views.index),
    path('search_name/', views.search_name),
    path('guest_manage/', views.guest_manage),
    path('search_phone/', views.search_phone),
    #path('sign_index/(?P<eid>[0-9]+)/', views.sign_index),#要匹配发布会id，不是固定的
    #path('logout/', views.logout),
    #sign system interface:
    #ex : /api/add_event/
    path('api/add_event/', views_if.add_event,name='add_event'),
    #ex:/api/add_guest/
    #url('add_guest/',views.if.add_guest,name='add_guest'),
    # ex:/api/get_event_list/
    path('api/get_event_list/',views_if.get_event_list),
    path('api/sec_get_event_list/',xiews_if_sec.sec_get_event_list),
    path('api/sec_add_event/',xiews_if_sec.sec_add_event),
    # ex:/api/get_guest_list/
    # url('get_guest_list/',views.if.get_guest_list),
    # ex:/api/user_sign/
    # url('user_sign/',views.if.user_sign,name='user_sign'),
]
