from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu_group, name='menu'),
    path('menu/<pk>/', views.menu_detail, name='menu_detail'),
]
