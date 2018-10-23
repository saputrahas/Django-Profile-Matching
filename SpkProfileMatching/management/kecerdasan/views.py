from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages

import pandas as pd
from orm.models import Karyawan, Kecerdasan, MasaKerja, PendidikanTerakhir, Prilaku, SikapKerja 
from management.kecerdasan import helpers







class ListKecerdasanView(View):
    def get(self, request):
        template = 'kecerdasan/index.html'
        krywn = Karyawan.objects.all()
        nl = helpers.ListKecerdasanNilai(krywn).as_matrix()
        data = {
            'nl' : nl,
        }
        return render(request, template, data)

class ListCfView(View):
    def get(self, request):
        template = 'kecerdasan/cf.html'
        krywn = Karyawan.objects.all()
        cf = helpers.CfKecerdasan(krywn).as_matrix()
        data = {
            'cf' : cf,
        }
        return render(request, template, data)

class ListSfView(View):
    def get(self, request):
        template = 'kecerdasan/sf.html'
        krywn = Karyawan.objects.all()
        sf = helpers.SfKecerdasan(krywn).as_matrix()
        data = {
            'sf' : sf,
        }
        return render(request, template, data)
 
class ListNiCfView(View):
     def get(self, request):
         template = 'kecerdasan/totalcf.html'
         krywn = Karyawan.objects.all()
         totalcf = helpers.NiCfKecerdasan(krywn).as_matrix()
         data = {
             'totalcf' : totalcf,
         }
         return render(request, template, data)
 
class ListNiSfView(View):
     def get(self, request):
         template = 'kecerdasan/totalsf.html'
         krywn = Karyawan.objects.all()
         totalsf = helpers.NiSfKecerdasan(krywn).as_matrix()
         data = {
             'totalsf' : totalsf,
         }
         return render(request, template, data)

class ListTotalView(View):
    def get(self, request):
        template = 'kecerdasan/total.html'
        krywn = Karyawan.objects.all()
        total = helpers.TotalKec(krywn).as_matrix()
        data =  {
            'total' : total,
        }
        return render(request, template, data)
