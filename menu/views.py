from django.shortcuts import render, get_object_or_404
from .models import Menu, Dish


def index(request):
    menus = Menu.objects.all()
    dishes = Dish.objects.all()
    return render(request, 'index.html', {'menus': menus, 'dishes': dishes})


def menu_detail(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    dishes = Dish.objects.all()
    return render(request, 'menu_detail.html', {'menu': menu,
                                                'dishes': dishes})
