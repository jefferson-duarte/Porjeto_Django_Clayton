from django.shortcuts import render
from django.http import HttpResponse


def exemplo(request):
    # return HttpResponse('Teste')
    return render(request, 'exemplo/index.html')
