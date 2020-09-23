from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd

from ..models.dashboardmodel import FillDashboard
from ..models.models import Core

# Create your views here.

def home(request):
    counter = FillDashboard()
    count = counter.filldashboardcounter()

    month = counter.filldashboardumfragenmonat()

    context = {**month, **count}
   
    return render(request, 'home.html', context)

def map_view(request):

    dataframe = Core()

    df = dataframe.createdataframeKMU()

    antworten = {
        'trifft nicht zu ': 0,
        'trifft eher nicht zu ' : 1,
        'trifft teilweise zu': 2, 
        'trifft teilweise zu ': 2,
        'trifft zu ': 3,
        'trifft zu':3,
    } 
    
    data_top = df.head()  
    
    for i in data_top:
        try:
            df['{}'.format(i)] = [antworten[item] for item in df['{}'.format(i)]]
            
        except:
            continue


    frame = df.iloc[:, 18:90]

    frame = frame.corr()

    frame = frame.to_html()

    context = {
        'frame' : frame,
    }

    return render(request, 'maps.html', context)

