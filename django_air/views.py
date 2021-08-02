from django.shortcuts import render 

from django.http import HttpResponse

from preprocessing import preprocessing
from OC1 import option_chain
from req import ex_date, keys_ce,keys_pe,nc
from post_processing import post_processing
import numpy as np
import os

import time

#import pickle

#import json

from io import StringIO
  
# Defining a function which
# will receive request and
# perform task depending 
# upon function definition
def OC (request) :
  
    # This will return Hello Geeks
    # string as HttpResponse
    return render(request , 'index_oc.html')

def CCS2(request):
    
    CCS = post_processing.call_calender_spread()
    
    tables={'CCS' : CCS.to_html()}
    
    return render(request, 'simple.html', context=tables)
