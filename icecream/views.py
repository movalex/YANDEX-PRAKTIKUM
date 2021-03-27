from django.http import HttpResponse
from .models import icecream_db


def icecream_list(request):
    # Получаем данные: полный список сортов мороженого
    db_query = icecream_db
    icecreams = f'Список мороженого: {db_query}'
    # Возвращаем результат в браузер пользователя
    return HttpResponse(icecreams)
