from django import forms
from .models import Setor, Empresa, Professor, Funcionario, Dadospessoais


class NovoSetorForm(forms.ModelForm):    
    class Meta:
        model = Setor
        fields = ['nome' ,'telefone', 'observacoes']
        
        
class LandingPageEmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['cnpj', 'nome_diretor', 'telefone', 'cep', 'email']


class NovoProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'telefone', 'cep', 'cidade', 'endereco', 'uf', 'bairro', 'numero', 'email', 'nome_da_mae', 'sexo', 'nacionalidade', 'data_nascimento', 'uf_naturalizado', 'cpf', 'rg', 'numero']


class NovoFuncionario(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'telefone', 'cep', 'cidade', 'endereco', 'uf', 'bairro', 'numero', 'email', 'nome_da_mae', 'sexo', 'nacionalidade', 'data_nascimento', 'uf_naturalizado', 'cpf', 'rg', 'numero']


class DadosPessoaisForm(forms.ModelForm):
    class Meta:
        model = Dadospessoais
        fields = '__all__'