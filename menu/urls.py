from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:menu_id>/', views.menu_detail, name='menu_detail'),
]
