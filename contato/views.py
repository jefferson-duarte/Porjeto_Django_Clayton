from django.shortcuts import render
from .contato_form import FormContato
from django.contrib import messages


def contato(request):
    return render(request, 'contato/contato.html', {'form': FormContato()})


def processa_contato(request):
    if request.method == 'POST':
        contato = FormContato(request.POST)
        if contato.is_valid():
            assunto = contato.cleaned_data['assunto']
            messages.success(request, 'Mensagem enviado com sucesso!')
            return render(request, 'contato/contato.html', {'form': FormContato()})  # noqa
        else:
            return render(request, 'contato/contato.html', {'form': contato})

    return render(request, 'contato/contato.html', {'form': FormContato()})
