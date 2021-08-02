# -*- coding: utf-8 -*-


from django.urls import path
from .views import OC, CCS2
app_name = 'django_air'

urlpatterns = [
    path('', OC, name = 'index_oc'),
    path('CCS/', CCS2),
]