from rest_framework import serializers
from .models import (
    Pagamento, Inadimplencia, HistoricoPagamento, Fatura,
    Desconto, Taxa, PagamentoTaxa, Multa, BolsaEstudo, Receita,
    Despesa, Transacao
)

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'

class InadimplenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inadimplencia
        fields = '__all__'

class HistoricoPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoPagamento
        fields = '__all__'

class FaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fatura
        fields = '__all__'
class DescontoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desconto
        fields = '__all__'

class TaxaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxa
        fields = '__all__'

class PagamentoTaxaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagamentoTaxa
        fields = '__all__'
class MultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multa
        fields = '__all__'

class BolsaEstudoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BolsaEstudo
        fields = '__all__'

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'

class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = '__all__'

class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = '__all__'
