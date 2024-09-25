from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.


def main_task1(request):
    page_name = 'Главная страница'
    context = {
        'page_name': page_name
    }
    return render(request, 'main.html', context)


def shop_task1(request):
    page_name = 'Магазин игр'
    back = "Вернуться назад"
    context = {
        'page_name': page_name,
        'games': Game.objects.all(),
        'back': back
    }
    return render(request, 'shop.html', context)


def cart_task1(request):
    page_name = 'Корзина'
    text = 'Тут пока ничего нет.'
    back = "Вернуться назад"
    context = {
        'page_name': page_name,
        'text': text,
        'back': back
    }
    return render(request, 'cart.html', context)


def sign_up_by_html(request):
    buyers = Buyer.objects.all()
    title = 'Регистрация'
    context = {'title': title}
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password != repeat_password:
            return HttpResponse('Пароли не совпадают')
        elif int(age) < 18:
            return HttpResponse('Вы должны быть старше 18 лет')
        for buyer in buyers:
            if username == buyer.name:
                return HttpResponse('Пользователь уже существует')
        Buyer.objects.create(name=username, balance=5000, age=age)
        return HttpResponse(f'Приветствуем {username}!')
    return render(request, 'registration_page.html', context)
