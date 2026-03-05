from django.apps import AppConfig
import pickle
import sys
import types
import pandas as pd
from django.conf import settings

# Patch de compatibilidade: pandas 2.x removeu pandas.core.indexes.numeric
# Os arquivos .pkl foram gerados com pandas 1.x e precisam desse módulo para desserializar
if 'pandas.core.indexes.numeric' not in sys.modules:
    _numeric_mod = types.ModuleType('pandas.core.indexes.numeric')
    _numeric_mod.Int64Index   = pd.Index
    _numeric_mod.Float64Index = pd.Index
    _numeric_mod.UInt64Index  = pd.Index
    sys.modules['pandas.core.indexes.numeric'] = _numeric_mod

class ViagemConfig(AppConfig): # Classe para o modelo de viagem
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'viagem'

    model        = pickle.load(open(settings.MEDIA_DATA + 'modelo_treinado.sav', 'rb')) # Carregando o modelo treinado
    travel_pivot = pickle.load(open(settings.MEDIA_DATA + 'travel_pivot.pkl', 'rb'))    # Carregando o dataset pivotado