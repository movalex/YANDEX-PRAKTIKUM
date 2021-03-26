from django.urls import path
from . import views

urlpatterns = [
    # этот path() сработает для запроса к адресу ''
    path('', views.index),
]