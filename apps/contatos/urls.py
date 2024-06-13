from django.urls import path
from apps.contatos.views import index, contato, buscar, novo_contato, deletar_contato, editar_contato

urlpatterns = [
    path('', index, name='index'),
    path('contato/<int:info_id>',contato, name='contato'),
    path('buscar', buscar, name= 'buscar'),
    path('novo-contato', novo_contato, name='novo_contato'),
    path('editar-contato/<int:info_id>', editar_contato, name='editar_contato'),
    path('deletar-contato/<int:info_id>', deletar_contato, name='deletar_contato'),

]