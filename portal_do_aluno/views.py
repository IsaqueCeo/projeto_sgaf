from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators  import has_permission_decorator
from core.models import Aluno, Disciplina
from gestao_escolar.models import Turma, FrequenciaDoAluno, BoletimDoAlunoPorDisciplina
from core.forms import DadosPessoaisForm
from django.contrib import messages

# Create your views here.

@login_required
@has_permission_decorator('atualizar_dados_pessoais_aluno') 
def atualizar_dados_pessoais_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    dados_pessoais = aluno.dados_pessoais
    template_name = 'aluno/atualizar-dados-pessoais-do-aluno.html'
    
    if request.method == "POST":
        form = DadosPessoaisForm(request.POST, request.FILES, instance=dados_pessoais)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados pessoais atualizados com sucesso!')
            return redirect('perfil-do-aluno')
    else:
        form = DadosPessoaisForm(instance=dados_pessoais)
    
    return render(request, template_name, {'form': form})


@login_required
@has_permission_decorator('listar_disciplinas_aluno') 
def listar_disciplinas_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    turmas = Turma.objects.get(alunos=aluno)
    disciplinas = set()
    for turma in turmas:
        for disciplina in turma.disciplinas.all():
            disciplinas.add(disciplina)
    
    return render(request, 'aluno/listar_disciplinas_aluno.html', {'aluno': aluno, 'disciplinas': disciplinas})


@login_required
@has_permission_decorator('consultar_frequencia_escolar_do_aluno') 
def consultar_frequencia_escolar_do_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    frequencia = FrequenciaDoAluno.objects.filter(aluno=aluno)
    template_name = 'aluno/frequencia-escolar-do-aluno.html'
    return render(request, template_name, {'frequencia': frequencia, 'aluno': aluno})




def consultar_frequencia_escolar_do_aluno_por_aula(request, id):
    ...


@login_required
@has_permission_decorator('consultar_minhas_notas_por_disciplina') 
def consultar_minhas_notas_por_disciplina(request, id, id_disciplina):
    template_name = 'aluno/notas-por-disciplina.html'
    aluno = get_object_or_404(Aluno, id=id)
    disciplina = Disciplina.objects.get(id=id_disciplina)
    boletim = BoletimDoAlunoPorDisciplina.objects.get(aluno=aluno, disciplina=disciplina)
    return render(request, template_name, {'aluno': aluno, 'boletim': boletim, 'disciplina': disciplina})
    