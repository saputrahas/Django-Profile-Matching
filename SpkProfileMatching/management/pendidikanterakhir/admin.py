from django.contrib import admin
from orm.models import PendidikanTerakhir

# Register your models here.
class PendidikanTerakhirAdmin(admin.ModelAdmin):
    pass
admin.site.register(PendidikanTerakhir, PendidikanTerakhirAdmin)

