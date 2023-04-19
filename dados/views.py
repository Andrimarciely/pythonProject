from django.shortcuts import render
from django.http import HttpResponse
from .models import SolicitacaoDeServico
from datetime import datetime, timedelta
from django.utils.timezone import localdate, now

def index(request):
    """Exibe todas as solicitações de serviços consolidados em uma única página. Não recebe parâmetros"""
    context = {
        'solicitacoes_de_servicos': SolicitacaoDeServico.objects.order_by('data_de_entrega_do_relatorio', 'prioridade'),
    }
    return render(request, 'solicitacoes_de_servicos.html', context)


def show(request, id):
    """Visualização de um determinado evento, recebe o 'id' do evento."""
    context = {
        'solicitacoes_de_servicos': SolicitacaoDeServico.objects.get(id=id),
    }
    return render(request, 'show.html', context)


def day(request, year, month, day):
    """Visualização dos eventos de um determinado dia, recebe a data em
    formato ano/mês/dia como parâmtro."""
    #
    day = datetime(year, month, day)
    context = {
        'today': localdate(),
        'day': day,
        'previous': day - timedelta(days=1),
        'next': day + timedelta(days=1),
        'solicitacoes_de_servicos': SolicitacaoDeServico.objects.filter(
            data_de_entrega_do_relatorio="{:%Y-%m-%d}".format(day)).order_by('-prioridade')
    }
    return render(request, 'day.html', context)
