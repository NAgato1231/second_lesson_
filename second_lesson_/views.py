from django.shortcuts import render


def index(request):
    name = 'Учиха Ыйман'
    return render(request, 'index.html', locals())

def index2(request):
    name = 'Сенджу Хаширама'
    return render(request, 'index2.html', locals())

def index3(request):
    name = 'Сенджу Тобирама'
    return render(request, 'index2.html', locals())

def index4(request):
    name = 'Учиха Мадара'
    return render(request, 'index2.html', locals())

def index5(request):
    name = 'Учиха Изуна'
    return render(request, 'index2.html', locals())