from django.views.generic import TemplateView

from ..models.exportmodels import Export
from ..models.models import Core

import pandas as pd

from django.http import HttpResponse
from io import BytesIO

# Create your views here.

class ExportView(TemplateView):
    template_name = 'export.html'

    def get_context_data(self, **kwargs):

        ex = Export()

        ex = ex.export()

        context = {
            'ex' : ex,
        }

        return context

def export_btn(request):
    with BytesIO() as b:
        # Use the StringIO object as the filehandle.
        df = Core()
        kmu = df.createdataframeKMU()
        ku = df.createdataframeKU()

        frames = [ku, kmu]

        df = pd.concat(frames)

        writer = pd.ExcelWriter(b, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1')
        writer.save()
        return HttpResponse(b.getvalue(), content_type='application/vnd.ms-excel')