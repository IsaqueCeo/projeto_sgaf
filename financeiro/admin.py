from django.contrib import admin
from .models import (
    Pagamento, Inadimplencia, HistoricoPagamento, Fatura,
    Desconto, Taxa, PagamentoTaxa, Multa, BolsaEstudo, Receita,
    Despesa, Transacao
)
# Register your models here.
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'valor_total', 'data_criacao', 'data_vencimento', 'data_pagamento', 'status')
    search_fields = ('aluno__nome', 'status')
    list_filter = ('status', 'data_criacao', 'data_vencimento', 'data_pagamento')

class InadimplenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'pagamento', 'data_vencimento', 'valor', 'status')
    search_fields = ('pagamento__aluno__nome', 'status')
    list_filter = ('status', 'data_vencimento')

class HistoricoPagamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'pagamento', 'valor_pago', 'data_pagamento', 'metodo_pagamento', 'status')
    search_fields = ('pagamento__aluno__nome', 'metodo_pagamento', 'status')
    list_filter = ('status', 'data_pagamento')

class FaturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'valor_total', 'data_emissao', 'data_vencimento', 'status')
    search_fields = ('aluno__nome', 'status')
    list_filter = ('status', 'data_emissao', 'data_vencimento')

    def get_valor_total(self, obj):
        return obj.valor_total
    get_valor_total.short_description = 'Valor Total'


class DescontoAdmin(admin.ModelAdmin):
    list_display = ('id', 'fatura', 'tipo', 'valor', 'data_concessao')
    search_fields = ('fatura__aluno__nome', 'tipo')
    list_filter = ('data_concessao',)

class TaxaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'valor', 'frequencia')
    search_fields = ('nome',)
    list_filter = ('frequencia',)

class PagamentoTaxaAdmin(admin.ModelAdmin):
    list_display = ('id', 'pagamento', 'taxa')
    search_fields = ('pagamento__aluno__nome', 'taxa__nome')

class MultaAdmin(admin.ModelAdmin):
    list_display = ('id', 'pagamento', 'valor', 'data_aplicacao', 'status')
    search_fields = ('pagamento__aluno__nome', 'status')
    list_filter = ('status', 'data_aplicacao')

class BolsaEstudoAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'tipo', 'valor', 'data_concessao')
    search_fields = ('aluno__nome', 'tipo')
    list_filter = ('data_concessao',)

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fonte', 'valor', 'data_recebimento', 'descricao')
    search_fields = ('fonte', 'descricao')
    list_filter = ('data_recebimento',)

class DespesaAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'valor', 'data_pagamento', 'descricao')
    search_fields = ('tipo', 'descricao')
    list_filter = ('data_pagamento',)

class TransacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'valor', 'data', 'descricao', 'get_relacionado_id', 'get_relacionado_tipo')
    search_fields = ('tipo', 'descricao', 'relacionado__tipo')
    list_filter = ('data', 'tipo')

    def get_relacionado_id(self, obj):
        return obj.relacionado.id if obj.relacionado else None
    get_relacionado_id.short_description = 'Relacionado ID'

    def get_relacionado_tipo(self, obj):
        return obj.relacionado.__class__.__name__ if obj.relacionado else None
    get_relacionado_tipo.short_description = 'Relacionado Tipo'



admin.site.register(Pagamento, PagamentoAdmin)
admin.site.register(Inadimplencia, InadimplenciaAdmin)
admin.site.register(HistoricoPagamento, HistoricoPagamentoAdmin)
admin.site.register(Fatura, FaturaAdmin)
admin.site.register(Desconto, DescontoAdmin)
admin.site.register(Taxa, TaxaAdmin)
admin.site.register(PagamentoTaxa, PagamentoTaxaAdmin)
admin.site.register(Multa, MultaAdmin)
admin.site.register(BolsaEstudo, BolsaEstudoAdmin)
admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Despesa, DespesaAdmin)
admin.site.register(Transacao, TransacaoAdmin)