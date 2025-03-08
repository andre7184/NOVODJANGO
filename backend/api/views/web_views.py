from django.shortcuts import render
from api.models import CustonUser

def home(request):
    user = CustonUser.objects.all()
    return render(request, 'home.html', {'usuarios': user})

def login(request):
    return render(request, 'login.html')

def CriarAluno(request):
    return render(request, 'criar_aluno.html')