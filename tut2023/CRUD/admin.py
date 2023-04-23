from django.contrib import admin
from .models import CRUD ,Pred
# Register your models here.
@admin.register(CRUD)
class CRUDCLASS(admin.ModelAdmin):
    list_display = ['id','image','firstname','lastname']

@admin.register(Pred)
class PredCLASS(admin.ModelAdmin):
    list_display = ['id', 'fid', 'prediction']
