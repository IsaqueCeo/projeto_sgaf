from django import forms
from gestao_escolar.models import FrequenciaDoAluno

class FrequenciaForms(forms.ModelForm):
    class Meta:
        model = FrequenciaDoAluno
        fields = ['aluno', 'aula', 'presenca']


            