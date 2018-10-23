from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages

from orm.models import Karyawan, Kecerdasan, MasaKerja, PendidikanTerakhir, Prilaku, SikapKerja 
import pandas as pd

from management.perangkingan import helpers

from reportlab.pdfgen import canvas
from django.template.loader import get_template


class ListTotalView(View):
    def get(self, request):
        template = 'perangkingan/index.html'
        krywn = Karyawan.objects.all()
        nl = helpers.total_rangking(krywn).as_matrix()
        data = {
            'nl' : nl,
        }
        return render(request, template, data)

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('perangkingan/report.html')
        krywn = Karyawan.objects.all()
        nl = helpers.total_rangking(krywn).as_matrix()
        data ={
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('perangkingan/report.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
