from django.shortcuts import render
from django.http import HttpResponse
from .models import SolicitacaoDeServico

def index(request):
    """Exibe todas as solicitações de serviços consolidados em uma única página. Não recebe parâmetros"""
    context = {
        'solicitacoes_de_servicos': SolicitacaoDeServico.objects.order_by('data_de_entrega_do_relatorio', 'prioridade'),
    }
    return render(request,'solicitacoes_de_servicos.html', context)

def show(request, id):
    """Visualização de um determinado evento, recebe o 'id' do evento."""
    context = {
            'event': SolicitacaoDeServico.objects.get(id=id),
            }
    return render(request, 'show.html', context)