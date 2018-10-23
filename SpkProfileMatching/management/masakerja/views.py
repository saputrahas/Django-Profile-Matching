from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages

import pandas as pd
from orm.models import Karyawan, Kecerdasan, MasaKerja, PendidikanTerakhir, Prilaku, SikapKerja 
from management.masakerja import helpers

class ListMasaKerjaView(View):
    def get(self, request):
        template = 'masakerja/index.html'
        krywn = Karyawan.objects.all()
        nlm = helpers.ListMasaKerjaNilai(krywn).as_matrix()
        data = {
            'nlm' : nlm,
        }
        return render(request, template, data)

class ListCfView(View):
    def get(self, request):
        template = 'masakerja/cf.html'
        krywn = Karyawan.objects.all()
        cf = helpers.CfMasaKerja(krywn).as_matrix()
        data = {
            'cf' : cf,
        }
        return render(request, template, data)

class ListSfView(View):
    def get(self, request):
        template = 'masakerja/sf.html'
        krywn = Karyawan.objects.all()
        sf = helpers.SfMasaKerja(krywn).as_matrix()
        data = {
            'sf' : sf,
        }
        return render(request, template, data)

class ListNiCfView(View):
     def get(self, request):
         template = 'masakerja/totalcf.html'
         krywn = Karyawan.objects.all()
         totalcf = helpers.NiCfMasaKerja(krywn).as_matrix()
         data = {
             'totalcf' : totalcf,
         }
         return render(request, template, data)

class ListNiSfView(View):
     def get(self, request):
         template = 'masakerja/totalsf.html'
         krywn = Karyawan.objects.all()
         totalsf = helpers.NiSfMasaKerja(krywn).as_matrix()
         data = {
             'totalsf' : totalsf,
         }
         return render(request, template, data)

class ListTotalView(View):
    def get(self, request):
        template = 'masakerja/total.html'
        krywn = Karyawan.objects.all()
        total = helpers.TotalMas(krywn).as_matrix()
        data =  {
            'total' : total,
        }
        return render(request, template, data)
