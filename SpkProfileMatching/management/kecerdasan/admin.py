from django.contrib import admin
from orm.models import Kecerdasan
# Register your models here.
class KecerdasanAdmin(admin.ModelAdmin):
    pass
admin.site.register(Kecerdasan, KecerdasanAdmin)