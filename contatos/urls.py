from django.urls import path
from contatos.views import index,contato

urlpatterns = [
    path('', index),
    path('contato/<int:info_id>',contato, name='contato')
]