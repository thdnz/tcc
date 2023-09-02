from django.urls import path
from . import views

urlpatterns = [ # Lista de URLs
    path('viagem/', views.index, name='index'), # URL para a página inicial
    path('recomendacao/', views.recomendacao, name='recomendacao'), # Adicionando a rota para a view de recomendação

]