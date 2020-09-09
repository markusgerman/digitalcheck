from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd

from ..models.dashboardmodel import FillDashboard
from ..models.models import Core

# Create your views here.

def home(request):
    counter = FillDashboard()
    context = counter.filldashboardcounter()
    
    return render(request, 'home.html', context)

def map_view(request):

    return render(request, 'maps.html')

