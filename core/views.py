from .models import Setor, Professor
from django.views.generic import CreateView, ListView
from .forms import NovoSetorForm, NovoProfessorForm, NovoFuncionario
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
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



###########################################################
###################### EMPRESA ############################
###########################################################





###########################################################
###################### SETOR ##############################
###########################################################


#Function Based View para criar um novo setor na minha empresa
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


#Function Based View para listar todos os setores da minha empresa
@login_required
def lista_setores(request):
    template_name = 'empresa/setores.html'
    empresa = request.user.funcionario.empresa
    setores = Setor.objects.filter(empresa=empresa)       
    context = {
        'setores': setores,
    }
    return render(request, template_name, context)


#Function Based View para atualizar um setor da minha empresa
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
            return redirect("atualizar-setor", id=id)
        else:
            return render(request, template_name, {'form': form})
    else:
        return render(request, template_name, {'form': form})


#Function Based View para deletar um setor da minha empresa
@login_required
def deletar_setor(request, id):
    empresa = request.user.funcionario.empresa
    setor = Setor.objects.get(id=id, empresa=empresa)
    setor.delete()
    return redirect('listar-setores')


#Function Based View para detalhar um setor da minha empresa
@login_required
def detalhar_setor(request, id):
    empresa = request.user.funcionario.empresa
    setor = Setor.objects.get(id=id, empresa=empresa )
    return render(request, 'empresa/detalhar-setor.html', {'setor':setor})



############################################################################
################################# PROFESSOR ##################################
############################################################################

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
    professores = Professor.objects.filter(empresa=empresa)
    professores.delete()
    return redirect('listar-professor')


@login_required
def detalhar_professor(request, id):
    empresa = request.user.funcionario.empresa
    professores = Professor.objects.filter(empresa=empresa)
    return render(request, 'empresa/detalhar-professor.html', {'professores':professores})


############################################################################
################################# FUNCIONÁRIO ###############################
############################################################################

@login_required
def novo_professor(request):
    if request.method == 'POST':
        form = NovoFuncionario(request.POST)
        if form.is_valid():
            professor = form.save(commit=False)
            professor.empresa = request.user.funcionario.empresa
            professor.save()
            messages.success(request, "Professor criado com sucesso!")
            return redirect('dashboard')
    else:
        form = NovoFuncionario()
        return render(request, 'empresa/novo-professor.html', {'form': form})


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
    professores = Professor.objects.filter(empresa=empresa)
    professores.delete()
    return redirect('listar-professor')


@login_required
def detalhar_professor(request, id):
    empresa = request.user.funcionario.empresa
    professores = Professor.objects.filter(empresa=empresa)
    return render(request, 'empresa/detalhar-professor.html', {'professores':professores})




############################################################################
################################## ALUNO ##################################
############################################################################


