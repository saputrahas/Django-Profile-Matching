from django.conf.urls import url
from management.perangkingan import views


urlpatterns = [
    url (r'^$', views.ListTotalView.as_view(), name='view'),
    url (r'^report$', views.GeneratePDF.as_view(), name='report'),
    # url (r'^print$', views.some_view, name='print'),
]