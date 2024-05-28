from django.urls import path
from contatos.views import index,contato,buscar

urlpatterns = [
    path('', index),
    path('contato/<int:info_id>',contato, name='contato'),
    path('buscar', buscar, name= 'buscar')
]