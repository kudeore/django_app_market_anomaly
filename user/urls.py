# -*- coding: utf-8 -*-

from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django_air.views import OC, CCS2
#app_name= 'django_air'
#namespace= 'django_air'
 
urlpatterns = [
         path('', views.index, name ='index'),
         path('', include( 'django_air.urls' )),
]