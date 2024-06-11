from django.contrib import admin
from apps.contatos.models import Contato

# Register your models here.


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'telefone', 'email')
admin.site.register(Contato, ContatoAdmin)