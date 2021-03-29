from django.shortcuts import render
from .models import icecream_db


# def icecream_list(request): # этот вариант не проходит проверку
#     context = {}
#     icecreams = ""
#     for i in range(len(icecream_db)):
#         icecreams += icecream_db[i]['name'] + "<br>"
#     context['icecreams'] = icecreams
#
#     return render(request, 'icecream/icecream-list.html', context=context)


def icecream_list(request):  # этот проходит
    icecreams = ''
    for i in range(len(icecream_db)):
        icecreams += f"{icecream_db[i]['name']}<br>"
        context = {'icecreams': icecreams}

    return render(request, 'icecream/icecream-list.html', context)
