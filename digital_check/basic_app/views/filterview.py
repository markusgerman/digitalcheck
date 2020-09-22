
from django.shortcuts import render

from ..models.models import Core

from ..models.filtermodel import Query

def filter_view(request, *args, **kwargs):
    stringlist = []

    if request.GET.get("checkbox1") == "on":
        stringlist.append('D2 == "Dienstleistung "')
    if request.GET.get("checkbox2") == "on":
        stringlist.append('D2 == "Handel"')
    if request.GET.get("checkbox3") == "on":
        stringlist.append('D2 == "Produzierendes Gewerbe"')
    if request.GET.get("checkbox4") == "on":
        stringlist.append('SurveyID == "313385"')
    if request.GET.get("checkbox5") == "on":
        stringlist.append('D1 == " 20-49 Mitarbeiter*innen"')
    if request.GET.get("checkbox6") == "on":
        stringlist.append('D1 == " 50-249 Mitarbeiter*innern"')
    if request.GET.get("checkbox7") == "on":
        stringlist.append('D1 == " ab 250 Mitarbeiter*innern"')

    quer = Query()

    value = quer.create(stringlist)

    context = {'value' : value}

    
    return render(request, 'filter.html', context)