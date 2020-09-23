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

    frame = df.to_html()

    context = {
        'frame' : frame,
    }

    return render(request, 'maps.html', context)

