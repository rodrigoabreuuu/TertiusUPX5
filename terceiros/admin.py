# Register your models here.

from django.contrib import admin
from .models import Colaborador
# 1. Importa a função de exportação que acabamos de criar
from .views import exportar_colaboradores_csv
 
# 2. Cria a classe de Admin customizada
class ColaboradorAdmin(admin.ModelAdmin):
    # Campos que serão exibidos na lista de colaboradores no admin
    list_display = ('nome', 'empresa_fornecedora', 'data_validade_contrato', 'status_conformidade')
    # Filtros laterais
    list_filter = ('status_conformidade', 'empresa_fornecedora')
 
    # Adiciona a função de exportação como uma ação
    actions = [exportar_colaboradores_csv]
 
    # Define o nome amigável da ação no menu suspenso
    exportar_colaboradores_csv.short_description = "Exportar Selecionados para CSV"
 
# 3. Registra o modelo usando a classe de Admin customizada
# Substitua a linha antiga (admin.site.register(Colaborador))
admin.site.register(Colaborador, ColaboradorAdmin)