from .models import Setor, Professor, Funcionario, Empresa, Aluno, Disciplina, SaladeAula, Dadospessoais
from .forms import NovoSetorForm, NovoProfessorForm, NovoFuncionario, EmpresaCompletaForm, AlunoForm, DadosPessoaisForm, ProfessorCompletoForm, FuncionarioCompletoForm
from .forms import AlunoCompletoForm, DisciplinaForm, SalaDeAulaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .utils import is_superuser
from rolepermissions.decorators  import has_permission_decorator
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


'''
VIEWS PARA EMPRESAS
'''


'''
VIEW ADMINISTRATIVA
Function Based View para criar uma nova empresa na plataforma
'''


@user_passes_test(is_superuser)
def cadastrar_empresa_adm(request):
    if request.method == 'POST':
        form = EmpresaCompletaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Empresa cadastrada com sucesso!")
            return redirect('dashboard')
    else:
        form = EmpresaCompletaForm() 

    return render(request, 'adm/cadastrar-empresa.html', {'form': form})


'''
VIEW ADMINISTRATIVA
Function Based View para listar todas as empresas na plataforma
'''


@user_passes_test(is_superuser)
def listar_empresas_cadastradas(request):
    template_name = 'adm/lista_empresas.html' 
    empresas = Empresa.objects.all()
    context = {
        'empresas': empresas,
    }
    return render(request, template_name, context)


'''
VIEW ADMINISTRATIVA
Function Based View para detalhar todas as empresas na plataforma
'''


@user_passes_test(is_superuser)
def detalhar_empresa_cadastrada(request, id):
    empresa = get_object_or_404(Empresa, id=id)
    return render(request, 'adm/detalhar_empresa.html', {'empresa': empresa})


'''
VIEW ADMINISTRATIVA
Function Based View para deletar uma empresa na plataforma
'''

@user_passes_test(is_superuser)
def deletar_empresa_cadastrada(request, id):
    empresa = get_object_or_404(Empresa, id=id)
    empresa.delete()
    messages.success(request, 'Empresa apagada com sucesso!')
    return redirect('listar-empresas-cadastradas')


'''
VIEW ADMINISTRATIVA
Function Based View para atualizar uma empresa na plataforma
'''

@user_passes_test(is_superuser)
def atualizar_empresa_cadastrada(request, id):
    
    empresa = get_object_or_404(Empresa, id=id)
    
    template_name = 'adm/atualizar_empresa_cadastrada.html'
    
    if request.method == "POST":
        form = EmpresaCompletaForm(request.POST, request.FILES, instance=empresa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empresa atualizada com sucesso!')
            return redirect('listar-empresas')
    else:
        form = EmpresaCompletaForm(instance=empresa)
    
    return render(request, template_name, {'form': form})


'''
VIEWS PARA SETOR DA EMPRESA
'''

'''
Function Based View para criar um novo setor na minha empresa
'''

@login_required
@has_permission_decorator('cadastrar_setor')
def novo_setor(request):
    if request.method == 'POST':
        form = NovoSetorForm(request.POST)
        if form.is_valid():
            setor = form.save(commit=False)
            setor.empresa = request.user.funcionario.empresa
            setor.save()
            messages.success(request, "Setor criado com sucesso!")
            return redirect('dashboard')
    else:
        form = NovoSetorForm()
    return render(request, 'empresa/setor.html', {'form': form})


'''
Function Based View para listar todos os setores na minha empresa
'''

@login_required
@has_permission_decorator('ver_setores')
def listar_setores(request):
    template_name = 'empresa/setores.html'
    try:
        empresa = request.user.funcionario.empresa
        setores = Setor.objects.filter(empresa=empresa)     
    except ObjectDoesNotExist:
        setores = Setor.objects.all()  
    context = {
        'setores': setores,
    }
    return render(request, template_name, context)


'''
Function Based View para atualizar um setor da minha empresa
'''


@login_required
@has_permission_decorator('atualizar_setor')
def atualizar_setor(request, id):
    empresa = request.user.funcionario.empresa
    setor = get_object_or_404(Setor, id=id, empresa=empresa)
    
    template_name = 'empresa/atualizar-setor.html'
    
    if request.method == "POST":
        form = NovoSetorForm(request.POST, instance=setor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Setor atualizado com sucesso!')
            return redirect('listar-setores')  
    else:
        form = NovoSetorForm(instance=setor)
    
    return render(request, template_name, {'form': form})


'''
Function Based View para deletar um setor da minha empresa
'''

@login_required
@has_permission_decorator('deletar_setor')
def deletar_setor(request, id):
    empresa = request.user.funcionario.empresa
    setor = get_object_or_404(Setor, id=id, empresa=empresa)
    setor.delete()
    messages.success(request, 'Setor deletado com sucesso!')
    return redirect('listar-setores')

'''
Function Based View para detalhar um setor da minha empresa
'''

@login_required
@has_permission_decorator('detalhar_setor')
def detalhar_setor(request, id):
    empresa = request.user.funcionario.empresa
    setor = get_object_or_404(Setor, id=id, empresa=empresa)    
    return render(request, 'empresa/detalhar-setor.html', {'setor':setor})



'''
VIEWS PARA PROFESSOR
'''

'''
Function Based View para cadastrar um Professor na minha empresa
'''


@login_required
@has_permission_decorator('novo_professor')
def novo_professor(request):
    if request.method == 'POST':
        form = NovoProfessorForm(request.POST)
        if form.is_valid():
            professor = form.save(commit=False)
            professor.empresa = request.user.funcionario.empresa
            professor.save()
            messages.success(request, "Professor criado com sucesso!")
            return redirect('dashboard')
    else:
        form = NovoProfessorForm()
        return render(request, 'empresa/novo-professor.html', {'form': form})

'''
Function Based View para listar todos os Professores na minha empresa
'''


@login_required
# @has_permission_decorator('listar_professores')
def listar_professores(request):
    template_name = 'empresa/listar-professores.html'
    try:
        empresa = request.user.funcionario.empresa
        professores = Professor.objects.filter(empresa=empresa)
    except ObjectDoesNotExist:
        professores = Professor.objects.all()
    context = {
        'professores': professores,
    }
    return render(request, template_name, context)


'''
Function Based View para atualizar um professor da minha empresa
'''

@login_required
@has_permission_decorator('atualizar_professor')
def atualizar_professor(request, id):
    empresa = request.user.funcionario.empresa
    professor = get_object_or_404(Professor, id=id, empresa=empresa)
    
    template_name = 'empresa/atualizar-professor.html'
    
    if request.method == "POST":
        form = ProfessorCompletoForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Professor atualizado com sucesso!')
            return redirect('listar-professores')  
    else:
        form = ProfessorCompletoForm(instance=professor)
    
    return render(request, template_name, {'form': form})
'''
Function Based View para deletar um professor da minha empresa
'''

@login_required
@has_permission_decorator('deletar_professor')
def deletar_professor(request, id):
    empresa = request.user.funcionario.empresa
    professor = get_object_or_404(Professor, empresa=empresa, id=id)    
    professor.delete()
    messages.success(request, 'Professor deletado com sucesso!')
    return redirect('listar-professor')

'''
Function Based View para detalhar um professor da minha empresa
'''

@login_required
@has_permission_decorator('detalhar_professor')
def detalhar_professor(request, id):
    empresa = request.user.funcionario.empresa
    professor = Professor.objects.get(empresa=empresa, id=id)  
    return render(request, 'empresa/detalhar-professor.html', {'professor':professor})


'''
VIEWS PARA FUNCIONÁRIOS DA EMPRESA
'''

'''
Function Based View para criar um novo funcionário na minha empresa
'''

@login_required
@has_permission_decorator('novo_funcionario')
def novo_funcionario(request):
    if request.method == 'POST':
        form = NovoFuncionario(request.POST)
        if form.is_valid():
            funcionario = form.save(commit=False)
            funcionario.empresa = request.user.funcionario.empresa
            funcionario.save()
            messages.success(request, "Funcionário criado com sucesso!")
            return redirect('dashboard')
    else:
        form = NovoFuncionario()
        return render(request, 'empresa/novo-funcionario.html', {'form': form})


'''
Function Based View para listar disciplinas na minha empresa
'''

@login_required
@has_permission_decorator('listar_funcionarios')
def listar_funcionarios(request):
    template_name = 'empresa/listar-funcionarios.html'
    empresa = request.user.funcionario.empresa
    funcionarios = Funcionario.objects.filter(empresa=empresa)
    context = {
        'funcionarios': funcionarios,
    }
    return render(request, template_name, context)


'''
Function Based View para atualizar funcionário na minha empresa
'''

@login_required
@has_permission_decorator('atualizar_funcionario')
def atualizar_funcionario(request, id):
    empresa = request.user.funcionario.empresa
    
    funcionario = get_object_or_404(Funcionario, id=id, empresa=empresa)
    
    form = FuncionarioCompletoForm(instance=funcionario)
    template_name = 'empresa/atualizar-funcionario.html'

    if request.method == "POST":
        form = FuncionarioCompletoForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Funcionário atualizado com sucesso!')
            return redirect('listar-funcionarios')  
        else:
            return render(request, template_name, {'form': form})
    else:
        return render(request, template_name, {'form': form})


'''
Function Based View para deletar funcionário na minha empresa
'''

@login_required
@has_permission_decorator('deletar_funcionario')
def deletar_funcionario(request, id):
    empresa = request.user.funcionario.empresa
    funcionario = get_object_or_404(Funcionario, empresa=empresa, id=id)
    funcionario.delete()
    messages.success(request, 'Funcionário deletado com sucesso!')
    return redirect('listar-funcionarios-da-empresa')



'''
Function Based View para detalhar funcionário na minha empresa
'''


@login_required
@has_permission_decorator('detalhar_funcionario')
def detalhar_funcionario(request, id):
    empresa = request.user.funcionario.empresa
    funcionario = get_object_or_404(Funcionario, empresa=empresa, id=id)
    return render(request, 'empresa/detalhar-funcionario.html', {'funcionario':funcionario})




'''
VIEWS PARA ALUNO
'''

'''
Function Based View para cadastrar um Aluno na minha empresa
'''

@login_required
@has_permission_decorator('criar_aluno')
def criar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.instituicao = request.user.funcionario.empresa
            aluno.save()
            messages.success(request, "Aluno criado com sucesso!")
            return redirect('dashboard')
    else:
        form = AlunoForm()
        
    return render(request, 'empresa/criar_aluno.html', {'form': form})
'''
Function Based View para listar todos os alunos na minha empresa
'''    

@login_required
@has_permission_decorator('listar_alunos')
def listar_alunos(request):
    template_name = 'empresa/listar_alunos.html'
    empresa = request.user.funcionario.empresa
    alunos = Aluno.objects.filter(instituicao=empresa)
    context = {
        'alunos': alunos,
    }
    return render(request, template_name, context)

'''
Function Based View para detalhar aluno na minha empresa
'''   

@login_required
@has_permission_decorator('detalhar_aluno')
def detalhar_aluno(request, id):
    empresa = request.user.aluno.empresa
    aluno = get_object_or_404(Aluno, instituicao=empresa, id=id)
    return render(request, 'empresa/detalhar-aluno.html', {'aluno': aluno})


'''
Function Based View para atualizar aluno na minha empresa
'''   

@login_required
@has_permission_decorator('atualizar_aluno')
def atualizar_aluno(request, id):
    empresa = request.user.funcionario.empresa    
    aluno = get_object_or_404(Aluno, id=id, instituicao=empresa)
    form = AlunoCompletoForm(instance=aluno)
    template_name = 'empresa/atualizar-aluno.html'
    
    if request.method == "POST":
        form = AlunoCompletoForm(request.POST, request.FILES, instance=aluno)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno atualizado com sucesso!')
            return redirect('listar-alunos')  
        else:
            return render(request, template_name, {'form': form})
    else:
        return render(request, template_name, {'form': form})


'''
Function Based View para deletar aluno na minha empresa
'''   
    
@login_required
@has_permission_decorator('deletar_aluno')
def deletar_aluno(request, id):
    empresa = request.user.funcionario.empresa
    aluno = get_object_or_404(Aluno, instituicao=empresa, id=id)
    aluno.delete()
    messages.success(request, 'Aluno deletado com sucesso!')
    return redirect('listar-alunos')




'''
VIEWS PARA DISCIPLINAS DA EMPRESA
'''

'''
Function Based View para criar uma nova Disciplina na minha empresa
'''

@login_required
@has_permission_decorator('criar_disciplina')
def criar_disciplina(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST, request=request)
        if form.is_valid():
            disciplina = form.save(commit=False)
            disciplina.instituicao = request.user.funcionario.empresa
            disciplina.save()
            messages.success(request, "Disciplina criada com sucesso!")
            return redirect('listar-disciplinas')
    else:
        form = DisciplinaForm(request=request)
    
    return render(request, 'empresa/nova-disciplina.html', {'form': form})

'''
Function Based View para listar disciplinas na minha empresa
'''

@login_required
@has_permission_decorator('listar_disciplinas')
def listar_disciplinas(request):
    template_name = 'empresa/listar-disciplinas.html'
    empresa = request.user.funcionario.empresa
    disciplinas = Disciplina.objects.filter(instituicao=empresa)
    context = {
        'disciplinas': disciplinas,
    }
    return render(request, template_name, context)


'''
Function Based View para deletar disciplina na minha empresa
'''   
    
@login_required
@has_permission_decorator('deletar_disciplina')
def deletar_disciplina(request, id):
    empresa = request.user.funcionario.empresa
    disciplina = get_object_or_404(Disciplina, instituicao=empresa, id=id)
    disciplina.delete()
    messages.success(request, 'Disciplina deletada com sucesso!')
    return redirect('listar-disciplinas')

'''
Function Based View para detalhar Disciplina na minha empresa
'''   

@login_required
@has_permission_decorator('detalhar_disciplina')
def detalhar_disciplina(request, id):
    empresa = request.user.funcionario.empresa
    disciplina = get_object_or_404(Disciplina, instituicao=empresa, id=id)
    return render(request, 'empresa/detalhar-disciplina.html', {'disciplina': disciplina})


'''
Function Based View para atualizar aluno na minha empresa
'''   

@login_required
@has_permission_decorator('atualizar_disciplina')
def atualizar_disciplina(request, id):
    empresa = request.user.funcionario.empresa    
    disciplina = get_object_or_404(Disciplina, id=id, instituicao=empresa)
    form = DisciplinaForm(instance=disciplina, request=request)
    template_name = 'empresa/atualizar-disciplina.html'
    
    if request.method == "POST":
        form = DisciplinaForm(request.POST, instance=disciplina, request=request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Disciplina atualizada com sucesso!')
            return redirect('listar-disciplinas')  
        else:
            return render(request, template_name, {'form': form})
    else:
        return render(request, template_name, {'form': form})
    

'''
Function Based View para ativar uma disciplina na minha empresa
'''

@login_required
@has_permission_decorator('ativar_disciplina') 
def ativar_disciplina(request, id):
    empresa = request.user.funcionario.empresa   
    disciplina = get_object_or_404(Disciplina, id=id, instituicao=empresa)
    if not disciplina.ativo:
        disciplina.ativo = True
        disciplina.save()
        messages.success(request, 'Disciplina foi ativada com sucesso!')
        return redirect('listar-disciplinas')
    else:
        messages.info(request, 'Disciplina já está ativa!')
        return redirect('listar-disciplinas')
    
'''
Function Based View para desativar uma disciplina na minha empresa
'''
@login_required
@has_permission_decorator('desativar_disciplina') 
def desativar_disciplina(request, id):
    empresa = request.user.funcionario.empresa   
    disciplina = get_object_or_404(Disciplina, id=id, instituicao=empresa)
    
    if disciplina.ativo:
        disciplina.ativo = False
        disciplina.save()
        messages.success(request, 'Disciplina foi desativada com sucesso!')
        return redirect('listar-disciplinas')
    else:
        messages.info(request, 'Disciplina já está desativada!')
        return redirect('listar-disciplinas')

'''
VIEWS PARA SALA DE AULA DA EMPRESA
'''

'''
Function Based View para criar uma nova Sala de Aula na minha empresa
'''

@login_required
@has_permission_decorator('criar_sala_de_aula') 
def criar_sala_de_aula(request):
    if request.method == 'POST':
        form = SalaDeAulaForm(request.POST, request.FILES)
        if form.is_valid():
            sala_de_aula = form.save(commit=False)
            sala_de_aula.instituicao = request.user.funcionario.empresa
            sala_de_aula.save()
            messages.success(request, "Sala de Aula criada com sucesso!")
            return redirect('listar-salas-de-aula')
    else:
        form = SalaDeAulaForm()
    
    return render(request, 'empresa/nova-sala-de-aula.html', {'form': form})

'''
Function Based View para listar as Salas de Aula na minha empresa
'''

@login_required
@has_permission_decorator('listar_salas_de_aula') 
def listar_salas_de_aula(request):
    template_name = 'empresa/listar-salas-de-aula.html'
    empresa = request.user.funcionario.empresa
    salas = SaladeAula.objects.filter(instituicao=empresa)
    context = {
        'salas': salas,
    }
    return render(request, template_name, context)


'''
Function Based View para deletar Salas de Aula na minha empresa
'''   
    
@login_required
@has_permission_decorator('deletar_sala_de_aula') 
def deletar_sala_de_aula(request, id):
    empresa = request.user.funcionario.empresa
    sala_de_aula = get_object_or_404(SaladeAula, instituicao=empresa, id=id)
    sala_de_aula.delete()
    messages.success(request, 'Sala de Aula deletada com sucesso!')
    return redirect('listar-salas-de-aula')

'''
Function Based View para detalhar Salas de Aula na minha empresa
'''   

@login_required
@has_permission_decorator('detalhar_sala_de_aula') 
def detalhar_sala_de_aula(request, id):
    empresa = request.user.funcionario.empresa
    sala = get_object_or_404(SaladeAula, instituicao=empresa, id=id)
    return render(request, 'empresa/detalhar-sala-de-aula.html', {'sala': sala})


'''
Function Based View para atualizar uma sala de aula na minha empresa
'''   

@login_required
@has_permission_decorator('atualizar_sala_de_aula') 
def atualizar_sala_de_aula(request, id):
    empresa = request.user.funcionario.empresa    
    sala = get_object_or_404(SaladeAula, instituicao=empresa, id=id)
    form = SalaDeAulaForm(instance=sala)
    template_name = 'empresa/atualizar-sala-de-aula.html'
    
    if request.method == "POST":
        form = SalaDeAulaForm(request.POST, request.FILES, instance=sala, request=request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sala de Aula atualizada com sucesso!')
            return redirect('listar-salas-de-aula')  
        else:
            return render(request, template_name, {'form': form})
    else:
        return render(request, template_name, {'form': form})
    
    
'''
Function Based View para marcar uma sala de aula como acessivel
'''

@login_required
@has_permission_decorator('marcar_sala_como_acessivel') 
def marcar_sala_como_acessivel(request, id):
    empresa = request.user.funcionario.empresa   
    sala = get_object_or_404(SaladeAula, id=id, instituicao=empresa)
    if not sala.acessibilidade:
        sala.acessibilidade = True
        sala.save()
        messages.success(request, 'Sala de Aula foi marcada com acessibilidade!')
        return redirect('listar-salas-de-aula')
    else:
        messages.info(request, 'Sala de Aula já foi estava marcada com acessibilidade!')
        return redirect('listar-salas-de-aula')
    
    
'''
Function Based View para marcar uma sala de aula como inacessivel
'''

@login_required
@has_permission_decorator('marcar_sala_como_inacessivel') 
def marcar_sala_como_inacessivel(request, id):
    empresa = request.user.funcionario.empresa   
    sala = get_object_or_404(SaladeAula, id=id, instituicao=empresa)
    
    if sala.acessibilidade:
        sala.acessibilidade = False
        sala.save()
        messages.success(request, 'Sala de Aula foi marcada como sem acessibilidade!')
        return redirect('listar-salas-de-aula')
    else:
        messages.info(request, 'Sala de Aula já estava marcada como sem acessibilidade!')
        return redirect('listar-salas-de-aula')