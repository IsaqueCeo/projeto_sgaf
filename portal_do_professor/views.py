from django.shortcuts import render, get_object_or_404, redirect
from core.models import Dadospessoais, Professor, Disciplina
from core.forms import DadosPessoaisForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators  import has_permission_decorator

# Create your views here.

def perfil_professor(request):
    ...


@login_required
@has_permission_decorator('atualizar_dados_pessoais_professor') 
def atualizar_dados_pessoais_professor(request, id):
    professor = get_object_or_404(Professor, id=id)
    dados_pessoais = professor.dados_pessoais
    template_name = 'professor/atualizar-dados-pessoais-do-professor.html'
    
    if request.method == "POST":
        form = DadosPessoaisForm(request.POST, request.FILES, instance=dados_pessoais)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados pessoais atualizados com sucesso!')
            return redirect('perfil-professor')
    else:
        form = DadosPessoaisForm(instance=dados_pessoais)
    
    return render(request, template_name, {'form': form})


def listar_disciplinas_do_professor(request, id):
    professor = get_object_or_404(Professor, id=id)
    disciplinas = Disciplina.objects.filter(professor=professor)
    template_name = 'professor/listar-disciplinas-do-professor.html'
    return render(request, template_name, {'disciplinas': disciplinas})