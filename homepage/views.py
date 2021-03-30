from django.shortcuts import render
from icecream.models import icecream_db
from anfisa.models import friends_db
# Импорт должен быть тут


def index(request):
    icecreams = ''
    friends = ''

    for friend in friends_db:
        # Узнайте город друга и сохраните его в city
        city = ...
        # Получите погоду из функции what_weather() и сохраните её в переменную weather
        weather = ...
        # Здесь через f-строку объедините переменные в одну строчку:
        # имя :: город :: погода
        friends += f'{friend} <br>'

    for i in range(len(icecream_db)):
        icecreams += (f'{icecream_db[i]["name"]} | '
                    f'<a href="icecream/{i}/">Узнать состав</a><br>')

    context = {
        'icecreams': icecreams,
        'friends': friends,
    }
    return render(request, 'homepage/index.html', context)
