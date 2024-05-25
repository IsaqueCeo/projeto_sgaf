from django import forms
from .models import Setor, Empresa


class NovoSetorForm(forms.ModelForm):    
    class Meta:
        model = Setor
        fields = ['nome' ,'telefone', 'observacoes']
        
        
class LandingPageEmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['cnpj', 'nome_diretor', 'telefone', 'cep', 'email']
