from django.db import models


class Parametro(models.Model):

    descricao_parametro = models.CharField(max_length=100, help_text='nome do agente químico')
    unidade_de_medida_do_parametro = models.CharField(max_length=10, help_text='unidade de medida do agente químico')
    resultado = models.CharField(max_length=10, help_text='valor mensurado do agente químico na amostra')
    lq = models.CharField(max_length=10, help_text='valor de referência')

    def __str__(self):
        return self.descricao_parametro