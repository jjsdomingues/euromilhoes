from django.shortcuts import render, redirect
from .models import Chave
import random

def index(request):
    return render(request, 'euroapp/index.html')

def gerar_chave(request):
    numeros = [str(i) for i in range(1, 51)]  # Lista de números de 1 a 50
    estrelas = [str(i) for i in range(1, 13)]  # Lista de estrelas de 1 a 12

    chave = Chave(numeros=', '.join(random.sample(numeros, 5)), estrelas=', '.join(random.sample(estrelas, 2)))
    chave.save()

    context = {
        'chave': chave,
    }

    return render(request, 'euroapp/gerar_chave.html', context)

def visualizar_chaves(request):
    chaves = Chave.objects.all()

    context = {
        'chaves': chaves,
    }

    return render(request, 'euroapp/visualizar_chaves.html', context)
