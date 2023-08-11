from django.apps import AppConfig
import pickle
from django.conf import settings

class ViagemConfig(AppConfig): # Classe para o modelo de viagem
    default_auto_field = 'django.db.models.BigAutoField' 
    name = 'viagem' 

    model           = pickle.load(open(settings.MEDIA_DATA + 'modelo_treinado.sav', 'rb')) # Carregando o modelo treinado
    travel_pivot    = pickle.load(open(settings.MEDIA_DATA + 'travel_pivot.pkl', 'rb')) # Carregando o dataset pivotado