from django.http import HttpResponse
from .models import icecream_db


def icecream_list(request):
    db_query = icecream_db
    icecream_list = [i['name'] for i in db_query]
    icecreams = f'Список сортов мороженого: {" :: ".join(icecream_list)}'
    return HttpResponse(icecreams)
