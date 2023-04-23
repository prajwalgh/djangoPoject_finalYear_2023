from django.urls import path
from . import views

urlpatterns = [
    path('CRUD2/', views.CRUD2, name='crud2'),
]