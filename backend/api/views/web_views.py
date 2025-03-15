from django.shortcuts import redirect, render

from ..models import CustomUser


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    user = CustomUser.objects.all()
    return render(request, 'home.html', {'usuarios': user})

def login(request):
    return render(request, 'login.html')

def criar_aluno(request,id=None):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        if id:
            usuario = CustomUser.objects.filter(id=id).first()
            if usuario:
                return render(request, 'criarAluno.html', {'aluno': usuario})   
            else:
                return redirect('CriarAluno') #o nome no redirect é dado pelo name colocado na rota no arquivo urls.py

        return render(request, 'criarAluno.html')
        