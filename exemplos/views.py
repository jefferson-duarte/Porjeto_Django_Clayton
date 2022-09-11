from django.shortcuts import render, redirect
from .form_exemplo import FormExemplo
from django.http import HttpResponse
import re


def exemplo(request):
    # return HttpResponse('Teste')

    return render(request, 'exemplo/02_form.html')
    # return render(request, 'exemplo/01_form.html')


# Executa as seguintes validações:
'''
    1. ter tamanho mínimo 6 e no máximo 15 caracteres.
    2. Deves ter somente letras e numero e caractere especial(!#@$%&)
    3. Deve ter no mínimo uma letra maiúscula e minúscula.
    4. Deve ter no mínimo um numero.
    5. Deve ter no mínimo caractere especial(!#@$%&)
'''


def validou_senha(senha):
    regex = '^(?=.*[A-Z])(?=.*[!#@$%&])(?=.*[0-9])(?=.*[a-z]).{6,15}$'
    if (re.search(regex, senha)):
        return True
    else:
        return False


# Faz validação do email utilizando regex
def validou_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  # noqa

    if (re.search(regex, email)):
        return True
    else:
        return False

# Caso email e senha tenha passado pela validação, retorna True


def validou_form(email, senha):
    if validou_email(email) and validou_senha(senha):
        return True
    else:
        return False


def processa_formulario(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    email_st = 'is-valid'
    senha_st = 'is-valid'

    if validou_form(email, senha):
        return redirect('/')
    else:
        if not validou_email(email):
            email_st = 'is-invalid'
        if not validou_senha(senha):
            senha_st = 'is-invalid'

    context = {
        'email': email,
        'senha': senha,
        'email_st': email_st,
        'senha_st': senha_st,
    }

    return render(request, 'exemplo/01_form.html', context)


def processa_formulario_v2(request):
    form = FormExemplo()

    if request.method == 'POST':
        form = FormExemplo(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            mensagem = form.cleaned_data['mensagem']

            return HttpResponse(f'Formulário validado com sucesso!!! - {email} - {senha} - {mensagem}')  # noqa
        else:
            print('Deu ruim.')

    context = {
        'form': form,
    }

    return render(request, 'exemplo/02_form.html', context)
