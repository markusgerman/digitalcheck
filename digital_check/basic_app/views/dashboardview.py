from django.shortcuts import render
from django.http import JsonResponse
from ..models.dashboardmodel import FillDashboard

# Create your views here.

def home(request):
    # context = {
    #     'ku' : ku,
    #     'kmu' : kmu,
    #     'umfragenM' : umfragenMonat,
    #     'umfragenG' : umfragenGesamt,
    # }
    
    return render(request, 'home.html')

def map_view(request):

    return render(request, 'maps.html')


def test_view(request):
    
    data = {
        'name': 'Vitorr',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    
    return JsonResponse(data)