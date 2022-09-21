from django.template.loader import render_to_string
from django.http import HttpResponse
from core import settings
from django.shortcuts import render
from .contato_form import FormContato
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from django.utils.html import strip_tags


def contato(request):
    return render(request, 'contato/contato.html', {'form': FormContato()})


def processa_contato(request):
    if request.method == 'POST':
        contato = FormContato(request.POST)
        if contato.is_valid():
            try:
                # enviar_email(contato)
                enviar_email_com_template(contato)
                obj_contato = contato.save()
                obj_contato.save()

                messages.success(request, 'Mensagem enviado com sucesso!')
                return render(request, 'contato/contato.html', {'form': FormContato()})  # noqa
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return render(request, 'contato/contato.html', {'form': FormContato()})  # noqa
        else:
            return render(request, 'contato/contato.html', {'form': contato})

    return render(request, 'contato/contato.html', {'form': FormContato()})


def enviar_email(contato):
    send_mail(
        contato.cleaned_data['assunto'],
        contato.cleaned_data['mensagem'],
        settings.EMAIL_HOST_USER,
        [contato.cleaned_data['email']],
        fail_silently=False
    )


def enviar_email_com_template(contato):
    html_content = render_to_string(
        'email_templates/confirmacao_mensagem.html',
        {
            'nome': contato.cleaned_data['nome'],
            'assunto': contato.cleaned_data['assunto'],
        }
    )
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(
        contato.cleaned_data['assunto'],
        text_content,
        settings.EMAIL_HOST_USER,
        [contato.cleaned_data['email']]
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    return True
