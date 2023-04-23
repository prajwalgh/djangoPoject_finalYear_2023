from django.urls import path
from . import views

urlpatterns = [
    path('CRUD/', views.CRUDV, name='crud'),
    path('1/', views.CRUDURL1, name='CRUDURL1'),


]