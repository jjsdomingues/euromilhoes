from django.urls import path
from . import views

app_name = 'euroapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('gerar_chave/', views.gerar_chave, name='gerar_chave'),
    path('visualizar_chaves/', views.visualizar_chaves, name='visualizar_chaves'),
]