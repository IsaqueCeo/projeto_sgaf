from .models import Setor, Professor, Funcionario, Empresa
from django.views.generic import CreateView, ListView
from .forms import NovoSetorForm, NovoProfessorForm, NovoFuncionario, EmpresaCompletaForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .utils import is_superuser

# Create your views here.

#Class Based View para criar um novo setor
# class NovoSetor(LoginRequiredMixin, CreateView):
#     model = Setor
#     template_name = 'empresa/setor.html'
#     form_class = NovoSetorForm
    
#     def form_valid(self, form):
#         form.instance.empresa = self.request.user.funcionario.empresa
#         return super().form_valid(form)
    
#     def get_success_url(self):
#         messages.add_message(self.request, messages.SUCCESS, "Setor criado com sucesso!")
#         return reverse('home')



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
    empresa = Empresa.objects.get(id=id)
    return render(request, 'adm/detalhar_empresa.html', {'empresa':empresa})


'''
VIEW ADMINISTRATIVA
Function Based View para deletar uma empresa na plataforma
'''

@user_passes_test(is_superuser)
def deletar_empresa_cadastrada(request, id):
    empresa = Empresa.objects.get(id=id)
    empresa.delete()
    return redirect('listar-empresas-cadastradas')


'''
VIEW ADMINISTRATIVA
Function Based View para atualizar uma empresa na plataforma
'''

@user_passes_test(is_superuser)
def atualizar_empresa_cadastrada(request, id):
    empresa = Empresa.objects.get(id=id)
    form = EmpresaCompletaForm(instance=empresa)
    if request.method == "POST":
        form = EmpresaCompletaForm(request.POST, request.FILES, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect("atualizar-empresa-cadastrada", id=id)
        else:
            return render(request, 'adm/atualizar_empresa_cadastrada.html', {'form': form})
    else:
        return render(request, 'adm/atualizar_empresa_cadastrada.html', {'form': form})



'''
VIEWS PARA SETOR DA EMPRESA
'''

'''
Function Based View para criar um novo setor na minha empresa
'''

@login_required
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
def listar_setores(request):
    template_name = 'empresa/setores.html'
    empresa = request.user.funcionario.empresa
    setores = Setor.objects.filter(empresa=empresa)       
    context = {
        'setores': setores,
    }
    return render(request, template_name, context)


'''
Function Based View para atualizar um setor da minha empresa
'''


@login_required
def atualizar_setor(request, id):
    empresa = request.user.funcionario.empresa
    setor = Setor.objects.get(id=id, empresa=empresa)
    form = NovoSetorForm(instance=setor)
    template_name = 'empresa/atualizar-setor.html'
    if request.method == "POST":
        form = NovoSetorForm(request.POST, instance=setor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Setor atualizado com sucesso!')
            return redirect("atualizar-setor", id=id)
        else:
            return render(request, template_name, {'form': form})
    else:
        return render(request, template_name, {'form': form})


'''
Function Based View para deletar um setor da minha empresa
'''

@login_required
def deletar_setor(request, id):
    empresa = request.user.funcionario.empresa
    setor = Setor.objects.get(id=id, empresa=empresa)
    setor.delete()
    return redirect('listar-setores')


'''
Function Based View para detalhar um setor da minha empresa
'''

@login_required
def detalhar_setor(request, id):
    empresa = request.user.funcionario.empresa
    setor = Setor.objects.get(id=id, empresa=empresa)
    return render(request, 'empresa/detalhar-setor.html', {'setor':setor})



'''
VIEWS PARA PROFESSOR
'''

'''
Function Based View para cadastrar um Professor na minha empresa
'''


@login_required
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
def listar_professor(request):
    template_name = 'empresa/listar-professores.html'
    empresa = request.user.funcionario.empresa
    professores = Professor.objects.filter(empresa=empresa)
    context = {
        'professores': professores,
    }
    return render(request, template_name, context)


@login_required
def atualizar_professor(request, id):
    empresa = request.user.funcionario.empresa
    professores = Professor.objects.filter(empresa=empresa)
    form = NovoProfessorForm(instance=professores)
    template_name = 'empresa/atualizar-professor.html'
    if request.method == "POST":
        form = NovoProfessorForm(request.POST, instance=professores)
        if form.is_valid():
            form.save()
            return redirect("atualizar-professor", id=id)
        else:
            return render(request, template_name, {'form': form})

@login_required
def deletar_professor(request, id):
    empresa = request.user.funcionario.empresa
    professor = Professor.objects.filter(empresa=empresa, id=id)
    professor.delete()
    return redirect('listar-professor')


@login_required
def detalhar_professor(request, id):
    empresa = request.user.funcionario.empresa
    professor = Professor.objects.get(id=id)  
    professor = Professor.objects.get(id=id)
    return render(request, 'empresa/detalhar-professor.html', {'professor':professor})


############################################################################
################################# FUNCIONÁRIO ###############################
############################################################################

@login_required
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


@login_required
def listar_funcionarios(request):
    template_name = 'empresa/listar-funcionarios.html'
    empresa = request.user.funcionario.empresa
    funcionarios = Funcionario.objects.filter(empresa=empresa)
    context = {
        'funcionarios': funcionarios,
    }
    return render(request, template_name, context)


@login_required
def atualizar_funcionario(request, id):
    empresa = request.user.funcionario.empresa
    professores = Funcionario.objects.filter(empresa=empresa)
    form = NovoProfessorForm(instance=professores)
    template_name = 'empresa/atualizar-professor.html'
    if request.method == "POST":
        form = NovoProfessorForm(request.POST, instance=professores)
        if form.is_valid():
            form.save()
            return redirect("atualizar-professor", id=id)
        else:
            return render(request, template_name, {'form': form})

@login_required
def deletar_funcionario(request, id):
    empresa = request.user.funcionario.empresa
    funcionario = Funcionario.objects.get(empresa=empresa, id=id)
    funcionario.delete()
    return redirect('listar-professor')


@login_required
def detalhar_professor(request, id):
    empresa = request.user.funcionario.empresa
    professores = Professor.objects.filter(empresa=empresa)
    return render(request, 'empresa/detalhar-professor.html', {'professores':professores})




############################################################################
################################## ALUNO ##################################
############################################################################


