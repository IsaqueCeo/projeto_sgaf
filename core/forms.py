from django import forms
from .models import Setor


class NovoSetorForm(forms.ModelForm):    
    class Meta:
        model = Setor
        fields = ['nome' ,'telefone', 'observacoes']
