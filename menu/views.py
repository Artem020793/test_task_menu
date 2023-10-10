from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu


def index(request):
    menu = Menu.objects.all()
    context = {
        'menu': menu,
    }
    return render(request, 'index.html', context)


def menu_group(request):
    return HttpResponse('Fuct 2')


def menu_detail(request):
    return HttpResponse('Furcr3')
