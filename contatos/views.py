
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


def buscar(request):
    contatos = Contato.objects.all()
    if 'buscar' in request.GET:
        nome = request.GET['buscar']
        if nome:
            contatos = Contato.objects.filter(nome__icontains=nome)
    return render(request, 'contatos/buscar.html', {'conts': contatos})

    
    
# Create your views here.
