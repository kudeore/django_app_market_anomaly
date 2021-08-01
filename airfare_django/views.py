# -*- coding: utf-8 -*-

from django.shortcuts import render 

from django.http import HttpResponse
  
# Defining a function which
# will receive request and
# perform task depending 
# upon function definition
def OC (request) :
  
    # This will return Hello Geeks
    # string as HttpResponse
    return render(request , 'index.html')