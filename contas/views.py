from django.shortcuts import render


def criar_conta(request):
    return render(request, 'contas/criar_conta.html')
