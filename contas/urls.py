from django.urls import path
from . import views

urlpatterns = [
    path('', views.criar_conta, name='criar_conta'),
]
