from django.contrib import admin
from .models import Parametro, Amostra, SolicitacaoDeServico, FormularioDeAmostra, ListaDeServico

admin.site.register(Parametro)
admin.site.register(Amostra)
admin.site.register(SolicitacaoDeServico)
admin.site.register(FormularioDeAmostra)
admin.site.register(ListaDeServico)