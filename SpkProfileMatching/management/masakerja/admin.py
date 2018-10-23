from django.contrib import admin
from orm.models import MasaKerja

# Register your models here.
class MasaKerjaAdmin(admin.ModelAdmin):
    pass
admin.site.register(MasaKerja, MasaKerjaAdmin)
