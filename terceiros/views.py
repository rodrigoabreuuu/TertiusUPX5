from django.shortcuts import render

# Create your views here.
from .models import Colaborador

from django.http import HttpResponse # NOVO: Para criar a resposta CSV
import csv # NOVO: Para formatar dados em CSV
 
def lista_colaboradores(request):
    # 1. Pega todos os colaboradores do banco de dados
    colaboradores = Colaborador.objects.all().order_by('nome')
 
    # 2. Envia os dados para o template exibir
    context = {
        'colaboradores': colaboradores,
        'titulo': 'Status dos Colaboradores Terceirizados'
    }
    return render(request, 'terceiros/lista_colaboradores.html', context)

def exportar_colaboradores_csv(modeladmin, request, queryset):
    # 1. Configura a resposta HTTP como um arquivo CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="colaboradores.csv"'
 
    writer = csv.writer(response)
 
    # 2. Escreve o cabeçalho do CSV
    writer.writerow(['Nome', 'Empresa Fornecedora', 'Data Validade Contrato', 'Status Conformidade'])
 
    # 3. Pega todos os dados e escreve linha por linha
    colaboradores = Colaborador.objects.all().values_list('nome', 'empresa_fornecedora', 'data_validade_contrato', 'status_conformidade')
    for colaborador in colaboradores:
        # Converte a data para um formato amigável 'DD/MM/AAAA' antes de escrever
        data_formatada = colaborador[2].strftime('%d/%m/%Y') if colaborador[2] else ''
        linha = list(colaborador)
        linha[2] = data_formatada # Substitui a data
        writer.writerow(linha)
 
    return response