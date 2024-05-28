from django.contrib import admin
from contatos.models import Contato

# Register your models here.


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'telefone', 'email')
admin.site.register(Contato, ContatoAdmin)