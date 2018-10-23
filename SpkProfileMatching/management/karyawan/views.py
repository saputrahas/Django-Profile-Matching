from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Karyawan
# Create your views here.

class ListKaryawanView(View):
    def get(self, request):
        template = 'karyawan/index.html'
        karyawan = Karyawan.objects.all()
        data = {

            'karyawan' : karyawan,
        }
        return render(request, template, data)