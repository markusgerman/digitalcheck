from django.shortcuts import render

from .models import FillDashboard

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