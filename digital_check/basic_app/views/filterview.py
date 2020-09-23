
from django.shortcuts import render
from ..models.models import Core
from ..models.filtermodel import Query

def filter_view(request, *args, **kwargs):
    
    stringlist1 = []
    if request.GET.get("checkbox1") == "on":
        stringlist1.append('D2 == "Dienstleistung "')
    if request.GET.get("checkbox2") == "on":
        stringlist1.append('D2 == "Handel"')
    if request.GET.get("checkbox3") == "on":
        stringlist1.append('D2 == "Produzierendes Gewerbe"')

    stringlist2 = []
    if request.GET.get("checkbox4") == "on":
        stringlist2.append('SurveyID == "313385"')
    if request.GET.get("checkbox5") == "on":
        stringlist2.append('D1 == " 20-49 Mitarbeiter*innen"')
    if request.GET.get("checkbox6") == "on":
        stringlist2.append('D1 == " 50-249 Mitarbeiter*innern"')
    if request.GET.get("checkbox7") == "on":
        stringlist2.append('D1 == " ab 250 Mitarbeiter*innern"')

    quer = Query()

    value = quer.create(stringlist1, stringlist2)


    context = {'value' : value}

    
    return render(request, 'filter.html', context)


from django.shortcuts import render

def days(request):
    
    week = Mymodel.objects.filter(created_on_gte=datetime.now()-timedelta(days=7)).count()
    yesterday = Mymodel.objects.filter(created_on_gte=datetime.now()-timedelta(days=1)).count()
    today = Mymodel.objects.filter(created_on_gte=datetime.now())

    context = {
        'week': week,
        'yesterday' : yesterday,
        'today' : today,
    }

    return render(request, 'days.html', context)
