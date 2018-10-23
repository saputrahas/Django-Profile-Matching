from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages

import pandas as pd
from orm.models import Karyawan, Kecerdasan, MasaKerja, PendidikanTerakhir, Prilaku, SikapKerja 
from management.pendidikanterakhir import helpers

class ListPendidikanTerakhirView(View):
    def get(self, request):
        template = 'pendidikanterakhir/index.html'
        krywn = Karyawan.objects.all()
        nlp = helpers.ListPendidikanTerakhir(krywn).as_matrix()
        data = {
            'nlp' : nlp,
        }
        return render(request, template, data)

class ListCfView(View):
    def get(self, request):
        template = 'pendidikanterakhir/cf.html'
        krywn = Karyawan.objects.all()
        cf = helpers.CfPenTer(krywn).as_matrix()
        data = {
            'cf' : cf,
        }
        return render(request, template, data)

class ListSfView(View):
    def get(self, request):
        template = 'pendidikanterakhir/sf.html'
        krywn = Karyawan.objects.all()
        sf = helpers.SfPenTer(krywn).as_matrix()
        data = {
            'sf' : sf,
        }
        return render(request, template, data)

class ListNiCfView(View):
     def get(self, request):
         template = 'pendidikanterakhir/totalcf.html'
         krywn = Karyawan.objects.all()
         totalcf = helpers.NiCfPenTer(krywn).as_matrix()
         data = {
             'totalcf' : totalcf,
         }
         return render(request, template, data)

class ListNiSfView(View):
     def get(self, request):
         template = 'pendidikanterakhir/totalsf.html'
         krywn = Karyawan.objects.all()
         totalsf = helpers.NiSfPenTer(krywn).as_matrix()
         data = {
             'totalsf' : totalsf,
         }
         return render(request, template, data)

class ListTotalView(View):
    def get(self, request):
        template = 'pendidikanterakhir/total.html'
        krywn = Karyawan.objects.all()
        total = helpers.TotalPenTer(krywn).as_matrix()
        data =  {
            'total' : total,
        }
        return render(request, template, data)