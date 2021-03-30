from django.shortcuts import render
# Здесь импортируйте icecream_db из файла models приложения icecream


def index(request):
    icecreams = ''
    for i in range(len(icecream_db)):
        # Измените строку, добавляемую к icecreams
        icecreams += f"<a href='icecream/{i}/'>{icecream_db[i]['name']}</a><br>"        
    context = {
        'icecreams': icecreams,
    }
    return render(request, 'homepage/index.html', context)
