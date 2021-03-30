from django.shortcuts import render
from icecream.models import icecream_db
# Здесь импортируйте словарь friends_db из файла anfisa/models.py


def index(request):
    icecreams = ''
    # Создайте пустую переменную friends 
    # Циклом обойдите словарь friends_db и сохраните все имена друзей в переменную friends
    for i in range(len(icecream_db)):
        icecreams += (f'{icecream_db[i]["name"]} |' 
                    f'<a href="icecream/{i}/">  Узнать состав</a><br>')
    context = {
        'icecreams': icecreams,
        # Добавьте переменную friends в словарь context
    }
    return render(request, 'homepage/index.html', context)
