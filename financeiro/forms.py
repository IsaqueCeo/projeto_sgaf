from django import forms
from financeiro.models import Mensalidade, Taxa, Fatura, Pagamento, Despesa, Faturamento

class MensalidadeForm(forms.ModelForm):
    class Meta:
        model = Mensalidade
        fields = ['serie', 'valor']

class TaxaForm(forms.ModelForm):
    class Meta:
        model = Taxa
        fields = ['juros', 'multa', 'tipo', 'valor_bolsa']

class FaturaForm(forms.ModelForm):
    class Meta:
        model = Fatura
        fields = ['aluno', 'valor_mensal', 'data_emissao', 'data_vencimento', 'status']

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['boleto', 'pago', 'status']

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['nome', 'categoria', 'valor', 'data', 'descricao', 'metodo']

class FaturamentoForm(forms.ModelForm):
    class Meta:
        model = Faturamento
        fields = ['nome', 'categoria', 'valor', 'data', 'descricao']
