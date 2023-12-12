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

    context = { # Dicionário com as viagens
        'viagens': Viagem.objects.all() # Lista de viagens
    }

    return render(request, 'viagem/index.html', context) # Renderiza a página index.html

def recomendacao(request): # View para a página de recomendação
    """ Recomendação de destino viajado """  
    valores_selecionados = request.POST.getlist('valor-recomendacao')

    lista_destinos = set()  # Conjunto de destinos

    for valor_selecionado in valores_selecionados:
        # Puxe o modelo treinado carregado do arquivo apps.py
        distances, suggestions = apps.ViagemConfig.model.kneighbors(
            apps.ViagemConfig.travel_pivot.loc[valor_selecionado, :].values.reshape(1, -1)
        )

        # Loop para percorrer a lista de sugestões
        for i in range(len(suggestions)):
            # Loop para percorrer a lista de destinos
            for j in apps.ViagemConfig.travel_pivot.index[suggestions[i]]:
                # Adiciona os destinos no conjunto
                lista_destinos.add(j)

    # Converta o conjunto de volta para uma lista
    lista_destinos = list(lista_destinos)

    context = {
        'destinos': lista_destinos
    }

    return render(request, 'viagem/recomendacao.html', context) # Renderiza a página recomendacao.html