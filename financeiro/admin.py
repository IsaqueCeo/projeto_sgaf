from django.contrib import admin
from .models import (
    Pagamento, Mensalidade, Fatura, Taxa, Despesa, Faturamento
)
# Register your models here.
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('id','boleto', 'pago', 'status')
    search_fields = ('boleto__fatura__aluno__nome', 'status')
    list_filter = ('status',)


class MensalidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'serie', 'valor')
    search_fields = ('serie',)
    list_filter = ('serie',)

class FaturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'valor_mensal', 'data_emissao', 'data_vencimento', 'status')
    search_fields = ('aluno__nome', 'status')
    list_filter = ('status', 'data_emissao', 'data_vencimento')

    def get_valor_total(self, obj):
        return obj.valor_total
    get_valor_total.short_description = 'Valor Total'


class TaxaAdmin(admin.ModelAdmin):
    list_display = ('id', 'juros', 'multa', 'tipo', 'valor_bolsa')



class FaturamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'valor', 'data', 'descricao')
    search_fields = ('nome', 'descricao')
    list_filter = ('data',)

class DespesaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'valor', 'data', 'descricao', 'metodo')
    search_fields = ('tipo', 'descricao', 'metodo')
    list_filter = ('data',)



    def get_relacionado_id(self, obj):
        return obj.relacionado.id if obj.relacionado else None
    get_relacionado_id.short_description = 'Relacionado ID'

    def get_relacionado_tipo(self, obj):
        return obj.relacionado.__class__.__name__ if obj.relacionado else None
    get_relacionado_tipo.short_description = 'Relacionado Tipo'



admin.site.register(Pagamento, PagamentoAdmin)
admin.site.register(Fatura, FaturaAdmin)
admin.site.register(Mensalidade, MensalidadeAdmin)
admin.site.register(Taxa, TaxaAdmin)
admin.site.register(Despesa, DespesaAdmin)
admin.site.register(Faturamento, FaturamentoAdmin)