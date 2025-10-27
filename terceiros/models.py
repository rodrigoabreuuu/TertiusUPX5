from django.db import models

# Create your models here.

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    empresa_fornecedora = models.CharField(max_length=100)
    data_validade_contrato = models.DateField()
    status_conformidade = models.CharField(max_length=50, default='Em Análise')

    def __str__(self):
        return self.nome