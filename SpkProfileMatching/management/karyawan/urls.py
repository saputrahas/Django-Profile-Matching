from django.conf.urls import url
from management.karyawan import views

urlpatterns = [
    url (r'^$', views.ListKaryawanView.as_view(), name='view'),
]