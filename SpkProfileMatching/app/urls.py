"""SpkProfileMatching URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from app.config import setting

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^karyawan/', include('management.karyawan.urls', namespace='karyawan')),
    url(r'^kecerdasan/', include('management.kecerdasan.urls', namespace='kecerdasan')),
    url(r'^masakerja/', include('management.masakerja.urls', namespace='masakerja')),
    url(r'^pendidikanterakhir/', include('management.pendidikanterakhir.urls', namespace='pendidikanterakhir')),
    url(r'^prilaku/', include('management.prilaku.urls', namespace='prilaku')),
    url(r'^sikapkerja/', include('management.sikapkerja.urls', namespace='sikapkerja')),
    url(r'^perangkingan/', include('management.perangkingan.urls', namespace='perangkingan')),





]

