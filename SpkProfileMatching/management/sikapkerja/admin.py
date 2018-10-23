from django.contrib import admin
from orm.models import SikapKerja

# Register your models here.
class SikapKerjaAdmin(admin.ModelAdmin):
    pass
admin.site.register(SikapKerja, SikapKerjaAdmin)
