from .models import Serie, Turma, FrequenciaDoAluno
from django import forms
from core.models import Aluno, Disciplina, SaladeAula
from django.forms import ModelChoiceField


class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ["serie", "turno"]
        


class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['disciplinas', 'ano_letivo', 'nome_turma', 'alunos', 'sala_de_aula', 'status', 'serie']
        
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        if request:
            empresa = request.user.funcionario.empresa
            self.fields['alunos'].queryset = Aluno.objects.filter(instituicao=empresa)            
            self.fields['disciplinas'].queryset = Disciplina.objects.filter(instituicao=empresa)
            self.fields['sala_de_aula'].queryset = SaladeAula.objects.filter(instituicao=empresa)

class FrequenciaForms(forms.ModelForm):
    class Meta:
        model = FrequenciaDoAluno
        fields = ['instituicao', 'aluno', 'aula', 'presenca']

        def __init__(self):
            return self.aluno
            
            
class NovaAulaForm(forms.ModelForm):
    ...

# class EmpresaFilteredModelChoiceField(ModelChoiceField):
#     def get_queryset(self, request):
#         empresa = request.user.funcionario.empresa
#         queryset = super().get_queryset()
#         return queryset.filter(instituicao=empresa)

# class TurmaForm(forms.ModelForm):
#     alunos = EmpresaFilteredModelChoiceField(
#         queryset=Aluno.objects.all(),
#         multiple=True,
#         required=False,
#         label='Alunos',
#     )
#     disciplinas = EmpresaFilteredModelChoiceField(
#         queryset=Disciplina.objects.all(),
#         multiple=True,
#         required=False,
#         label='Disciplinas',
#     )
#     sala_de_aula = EmpresaFilteredModelChoiceField(
#         queryset=SaladeAula.objects.all(),
#         required=False,
#         label='Sala de Aula',
#     )