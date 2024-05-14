
from django.shortcuts import render, get_object_or_404

from django.urls import path
from contatos.models import Contato

# Create your views here.
def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', {"conts": contatos})
    

def contato(request, info_id):
    contato = get_object_or_404(Contato, pk =info_id)
    return render(request, 'contatos/det_contato.html', {"contato": contato})
    
    
# Create your views here.
