from django.contrib import admin
from orm.models import Karyawan

class KaryawanAdmin(admin.ModelAdmin):
    pass
admin.site.register(Karyawan, KaryawanAdmin)
