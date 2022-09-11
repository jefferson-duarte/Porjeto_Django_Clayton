from django.urls import path
from . import views

urlpatterns = [
    path('contato/', views.contato, name='contato'),
    path('mensagem/', views.processa_contato, name='mensagem'),
]
