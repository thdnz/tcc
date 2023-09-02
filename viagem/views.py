from django.shortcuts import render 
from django.http import HttpResponseRedirect, request
from django.urls import reverse 
from .models import Viagem # Importando o modelo de viagem
from . import apps
import pickle # Importando o módulo pickle
from django.conf import settings

# Create your views here. # Criando a view para o formulário de cadastro de viagem
def index(request): # View para a página inicial
    """ Lista de viagens """ 

    if not request.user.is_authenticated: # Verifica se o usuário está logado
        return  HttpResponseRedirect(reverse('login')) 

    context = { # Dicionário com as viagens
        'viagens': Viagem.objects.all() # Lista de viagens
    }

    return render(request, 'viagem/index.html', context) # Renderiza a página index.html

def recomendacao(request): # View para a página de recomendação
    """ Recomendação de destino viajado """ 
    if not request.user.is_authenticated:
        return  HttpResponseRedirect(reverse('login'))  
    #puxa o modelo treinado carregado do arquivo apps.py
    distances, suggestions = apps.ViagemConfig.model.kneighbors(apps.ViagemConfig.travel_pivot.loc[request.POST['valor-recomendacao'], :].values.reshape(1, -1))

    lista_destinos = [] # Lista de destinos
    for i in range(len(suggestions)): # Loop para percorrer a lista de sugestões
        for j in apps.ViagemConfig.travel_pivot.index[suggestions[i]]: # Loop para percorrer a lista de destinos
            lista_destinos.append(j) # Adiciona os destinos na lista

    context = { # Dicionário com os destinos
        'destinos': lista_destinos # Lista de destinos
    }

    return render(request, 'viagem/recomendacao.html', context) # Renderiza a página recomendacao.html