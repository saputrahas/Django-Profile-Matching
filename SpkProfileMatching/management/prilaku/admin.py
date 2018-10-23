from django.contrib import admin
from orm.models import Prilaku

# Register your models here.
class PrilakuAdmin(admin.ModelAdmin):
    pass
admin.site.register(Prilaku, PrilakuAdmin)
