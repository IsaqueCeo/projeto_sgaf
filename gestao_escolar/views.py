from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SerieForm, TurmaForm
from django.contrib import messages
from .models import Serie, Turma
from rolepermissions.decorators  import has_permission_decorator
# Create your views here.

'''
VIEWS PARA SERIE

'''

'''
Function Based View para criar uma nova serie na empresa
'''


@login_required
@has_permission_decorator('cadastrar_nova_serie') 
def cadastrar_nova_serie(request):
    if request.method == 'POST':
        form = SerieForm(request.POST)
        if form.is_valid():
            serie = form.save(commit=False)
            serie.empresa = request.user.funcionario.empresa  
            serie.save()
            messages.success(request, "Série criada com sucesso!")
            return redirect('listar-series')  
    else:
        form = SerieForm() 

    context = {'form': form}
    return render(request, 'empresa/cadastrar-serie.html', context)


'''
Function Based View para listar todos os setores na minha empresa
'''

@login_required
@has_permission_decorator('listar_series') 
def listar_series(request):
    template_name = 'empresa/lista_de_series.html'
    empresa = request.user.funcionario.empresa
    series = Serie.objects.filter(instituicao=empresa)       
    context = {
        'series': series,
    }
    return render(request, template_name, context)

'''
Function Based View para atualizar uma serie da minha empresa
'''


@login_required
@has_permission_decorator('atualizar_serie') 
def atualizar_serie(request, id):
    empresa = request.user.funcionario.empresa
    serie = get_object_or_404(Serie, id=id, instituicao=empresa)
    template_name = 'empresa/atualizar-serie.html'
    
    if request.method == "POST":
        form = SerieForm(request.POST, instance=serie)
        if form.is_valid():
            form.save()
            messages.success(request, 'Série atualizada com sucesso!')
            return redirect('listar-series') 
    else:
        form = SerieForm(instance=serie)
    
    return render(request, template_name, {'form': form})


'''
Function Based View para detalhar uma serie da minha empresa
'''

@login_required
@has_permission_decorator('detalhar_serie') 
def detalhar_serie(request, id):
    empresa = request.user.aluno.empresa
    serie = get_object_or_404(Serie, instituicao=empresa, id=id)
    return render(request, 'empresa/detalhar-serie.html', {'serie': serie})

'''
Function Based View para detalhar uma serie da minha empresa
'''

@login_required
@has_permission_decorator('deletar_serie') 
def deletar_serie(request, id):
    empresa = request.user.funcionario.empresa
    serie = get_object_or_404(Serie, instituicao=empresa, id=id)
    serie.delete()
    messages.success(request, 'Aluno deletado com sucesso!')
    return redirect('listar-series')

'''
VIEWS PARA TURMA

'''

'''
Function Based View para criar uma turma na empresa
'''


@login_required
def criar_turma(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST, empresa=request.user.funcionario.empresa)
        if form.is_valid():
            turma = form.save(commit=False)
            turma.instituicao = request.user.funcionario.empresa
            turma.save()
            form.save_m2m() 
            return redirect('listar-turmas')
    else:
        form = TurmaForm(empresa=request.user.funcionario.empresa)
        
    return render(request, 'empresa/criar_turma.html', {'form': form})


'''
Function Based View para listar todos as turmas na minha empresa
'''

@login_required
def listar_turmas(request):
    template_name = 'empresa/lista_de_turmas.html'
    empresa = request.user.funcionario.empresa
    turmas = Turma.objects.filter(instituicao=empresa)       
    context = {
        'turmas': turmas,
    }
    return render(request, template_name, context)


'''
Function Based View para detalhar uma turma da minha empresa
'''

@login_required
def detalhar_turma(request, id):
    empresa = request.user.aluno.empresa
    turma = get_object_or_404(Turma, instituicao=empresa, id=id)
    return render(request, 'empresa/detalhar-turma.html', {'turma': turma})


'''
Function Based View para deletar uma turma da minha empresa
'''

@login_required
def deletar_turma(request, id):
    empresa = request.user.funcionario.empresa
    turma = get_object_or_404(Turma, instituicao=empresa, id=id)
    turma.delete()
    messages.success(request, 'Turma deletada com sucesso!')
    return redirect('listar-turmas')

'''
Function Based View para atualizar uma turma da minha empresa
'''

@login_required
def atualizar_turma(request, id):
    empresa = request.user.funcionario.empresa
    turma = get_object_or_404(Turma, id=id, instituicao=empresa)
    template_name = 'empresa/atualizar-turma.html'
    
    if request.method == "POST":
        form = TurmaForm(request.POST, instance=turma, empresa=request.user.funcionario.empresa)
        if form.is_valid():
            form.save()
            form.save_m2m() 
            messages.success(request, 'Turma atualizada com sucesso!')
            return redirect('listar-turmas') 
    else:
        form = TurmaForm(instance=turma, empresa=request.user.funcionario.empresa)
    
    return render(request, template_name, {'form': form})
