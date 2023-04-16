from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='solicitacoes-de-servicos-all'),
    path('<int:id>', views.show, name='solicitacao-de-servico-show'),
    path('<int:year>/<int:month>/<int:day>', views.day, name='solicitacao-de-servico-day'),
    ]
