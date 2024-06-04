from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroForms  

# Create your views here.
def login(request):
    form = LoginForms()  
    return render(request, 'usuarios/login.html', {'form': form})  

def logout(request):
    return render(request, 'usuarios/logout.html')  

def cadastrar(request):
    form = CadastroForms()
    return render(request, 'usuarios/cadastrar.html', {'form': form})