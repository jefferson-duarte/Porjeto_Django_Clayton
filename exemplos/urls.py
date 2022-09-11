from django.urls import path
from . import views

urlpatterns = [
    path('', views.exemplo, name='exemplo'),
    path('processa_formulario/', views.processa_formulario, name='processa_formulario'),  # noqa
    path('processa_formulario_v2/', views.processa_formulario_v2, name='processa_formulario_v2'),  # noqa
]
