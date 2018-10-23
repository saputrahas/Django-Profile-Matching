from django.conf.urls import url
from management.pendidikanterakhir import views


urlpatterns = [
    url (r'^$', views.ListPendidikanTerakhirView.as_view(), name='view'),
    url (r'^cf$', views.ListCfView.as_view(), name='cf'),
    url (r'^sf$', views.ListSfView.as_view(), name='sf'),
    url (r'^totalcf$', views.ListNiCfView.as_view(), name='totalcf'),
    url (r'^totalsf$', views.ListNiSfView.as_view(), name='totalsf'),
    url (r'^total$', views.ListTotalView.as_view(), name='total'),

]