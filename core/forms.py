from django import forms
from .models import Setor, Empresa, Professor, Funcionario, Dadospessoais, Aluno


class NovoSetorForm(forms.ModelForm):    
    class Meta:
        model = Setor
        fields = ['nome' ,'telefone', 'observacoes']
        
        
class LandingPageEmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['cnpj', 'nome_diretor', 'telefone', 'cep', 'email']
        
class EmpresaCompletaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'


class NovoProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'telefone', 'cep', 'cidade', 'endereco', 'uf', 'bairro', 'numero', 'email', 'nome_da_mae', 'sexo', 'nacionalidade', 'data_nascimento', 'uf_naturalizado', 'cpf', 'rg', 'numero']


class ProfessorCompletoForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'

class NovoFuncionario(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'telefone', 'cep', 'cidade', 'endereco', 'uf', 'bairro', 'numero', 'email', 'nome_da_mae', 'sexo', 'nacionalidade', 'data_nascimento', 'uf_naturalizado', 'cpf', 'rg', 'numero']



class FuncionarioCompletoForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'

class DadosPessoaisForm(forms.ModelForm):
    class Meta:
        model = Dadospessoais
        fields = '__all__'


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'telefone', 'sexo', 'endereco', 'cep', 'uf', 'numero', 'bairro', 'cidade']