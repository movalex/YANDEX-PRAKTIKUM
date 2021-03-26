from django.urls import path
from . import views


urlpatterns = [
    # здесь должен быть path(), который
    # при обращении к странице /icecream/
    # вызовет функцию icecream_list() из views.py
    # # [примечание] при include запрошенный URL в присоединяемом файле
    # указывается не полностью
    path('', views.icecream_list)
]
