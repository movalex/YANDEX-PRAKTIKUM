from django.http import HttpResponse

# тут должна быть view-функция icecream_list(), но её нет
# не забудьте про обязательный аргумент request


def icecream_list(request):
    return HttpResponse('Здесь будет список сортов мороженого')