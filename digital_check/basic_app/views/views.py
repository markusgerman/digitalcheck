from django.shortcuts import render

from ..models.models import FillDashboard

# Create your views here.

def home(request):

    diagramm = FillDashboard()
    ku = diagramm.getallumfrageteilnehmer("ku")
    kmu = diagramm.getallumfrageteilnehmer("kmu")

    umfragenMonat = diagramm.getumfrageteilnehmerlastweek()

    umfragenGesamt = ku + kmu
    

    context = {
        'ku' : ku,
        'kmu' : kmu,
        'umfragenM' : umfragenMonat,
        'umfragenG' : umfragenGesamt,
    }
    
    return render(request, 'home.html', context)

def map_view(request):

    return render(request, 'maps.html')


from django.http import JsonResponse

def test_view(request):
    
    data = {
        'name': 'Vitorr',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    
    return JsonResponse(data)