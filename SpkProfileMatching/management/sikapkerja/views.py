from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages

import pandas as pd
from orm.models import Karyawan, Kecerdasan, MasaKerja, PendidikanTerakhir, Prilaku, SikapKerja 
from management.sikapkerja import helpers

class ListSikapKerjaView(View):
    def get(self, request):
        template = 'sikapkerja/index.html'
        krywn = Karyawan.objects.all()
        nlp = helpers.ListSikapKerja(krywn).as_matrix()
        data = {
            'nlp' : nlp,
        }
        return render(request, template, data)

class ListCfView(View):
    def get(self, request):
        template = 'sikapkerja/cf.html'
        krywn = Karyawan.objects.all()
        cf = helpers.CfSikapKerja(krywn).as_matrix()
        data = {
            'cf' : cf,
        }
        return render(request, template, data)

class ListSfView(View):
    def get(self, request):
        template = 'sikapkerja/sf.html'
        krywn = Karyawan.objects.all()
        sf = helpers.SfSikapKerja(krywn).as_matrix()
        data = {
            'sf' : sf,
        }
        return render(request, template, data)

class ListNiCfView(View):
     def get(self, request):
         template = 'sikapkerja/totalcf.html'
         krywn = Karyawan.objects.all()
         totalcf = helpers.NiCfSik(krywn).as_matrix()
         data = {
             'totalcf' : totalcf,
         }
         return render(request, template, data)

class ListNiSfView(View):
     def get(self, request):
         template = 'sikapkerja/totalsf.html'
         krywn = Karyawan.objects.all()
         totalsf = helpers.NiSfSik(krywn).as_matrix()
         data = {
             'totalsf' : totalsf,
         }
         return render(request, template, data)

class ListTotalView(View):
    def get(self, request):
        template = 'sikapkerja/total.html'
        krywn = Karyawan.objects.all()
        total = helpers.TotalSik(krywn).as_matrix()
        data =  {
            'total' : total,
        }
        return render(request, template, data)
