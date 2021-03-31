from django.shortcuts import render
from icecream.models import icecream_db
from anfisa.models import friends_db
from anfisa.services import what_weather


def index(request):
    icecreams = ''
    friends = ''
    city_weather = ''
    friend_output = ''
    # Добавлена пустая  переменная для хранения сорта мороженого, полученного из запроса
    selected_icecream = ''

    for friend in friends_db:
        # Около каждого имени вставляется radio button,
        # и теперь в форме кликом по кнопочке можно будет выбрать одного из друзей.

        friends += (f'<input type="radio" name="friend"'
                    f' required value="{friend}">{friend}<br>')

    for i in range(len(icecream_db)):
        # В переменную ice_form добавьте HTML-код радио-кнопки и название мороженого
        # (за образец можно взять код для списка друзей)
        icecream_name = icecream_db[i]["name"]
        ice_form = f'<input type="radio" name="icecream" required value="{icecream_name}">{icecream_name}'
        ice_link = f'<a href="icecream/{i}/">Узнать состав</a>'
        icecreams += f'{ice_form} | {ice_link} <br>'

    if request.method == 'POST':
        selected_friend = request.POST['friend']
        selected_icecream = request.POST['icecream']
        city = friends_db[selected_friend]
        weather = what_weather(city)
        # Вместо слова "мороженое" выведите название сорта из запроса.
        friend_output = f'{selected_friend}, тебе прислали {selected_icecream}!'
        city_weather = f'Погода в городе {city}: {weather}'

    context = {
        'icecreams': icecreams,
        'friends': friends,
        'friend_output': friend_output,
        'city_weather': city_weather,
    }
    return render(request, 'homepage/index.html', context)
