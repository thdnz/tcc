from django.db import models

# Create your models here.
class Viagem(models.Model): # Classe para o modelo de viagem
    DESTINO = ( # Lista de destinos
        ('bento_goncalves', 'Bento Gonçalves'), 
        ('bonito', 'Bonito')
    )

    destino = models.CharField(choices=DESTINO, max_length=255) # Campo de destino