from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages

import pandas as pd
from orm.models import Karyawan, Kecerdasan, MasaKerja, PendidikanTerakhir, Prilaku, SikapKerja 
from management.prilaku import helpers

class ListPrilakuView(View):
    def get(self, request):
        template = 'prilaku/index.html'
        krywn = Karyawan.objects.all()
        nlp = helpers.ListPrilaku(krywn).as_matrix()
        data = {
            'nlp' : nlp,
        }
        return render(request, template, data)

class ListCfView(View):
    def get(self, request):
        template = 'prilaku/cf.html'
        krywn = Karyawan.objects.all()
        cf = helpers.CfPrilaku(krywn).as_matrix()
        data = {
            'cf' : cf,
        }
        return render(request, template, data)

class ListSfView(View):
    def get(self, request):
        template = 'prilaku/sf.html'
        krywn = Karyawan.objects.all()
        sf = helpers.SfPrilaku(krywn).as_matrix()
        data = {
            'sf' : sf,
        }
        return render(request, template, data)

class ListNiCfView(View):
     def get(self, request):
         template = 'prilaku/totalcf.html'
         krywn = Karyawan.objects.all()
         totalcf = helpers.NiCfPri(krywn).as_matrix()
         data = {
             'totalcf' : totalcf,
         }
         return render(request, template, data)

class ListNiSfView(View):
     def get(self, request):
         template = 'prilaku/totalsf.html'
         krywn = Karyawan.objects.all()
         totalsf = helpers.NiSfPri(krywn).as_matrix()
         data = {
             'totalsf' : totalsf,
         }
         return render(request, template, data)

class ListTotalView(View):
    def get(self, request):
        template = 'prilaku/total.html'
        krywn = Karyawan.objects.all()
        total = helpers.TotalPri(krywn).as_matrix()
        data =  {
            'total' : total,
        }
        return render(request, template, data)
