from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=100 , null=False, blank=False)
    telefone  = models.CharField(max_length =100, null=False, blank=False)
    email =  models.EmailField(max_length = 254, null=False, blank=False)
    endereco = models.CharField(max_length=254)
    imagem = models.CharField(max_length= 254, null=True, blank=True)


def __str__(self):
     return self.nome