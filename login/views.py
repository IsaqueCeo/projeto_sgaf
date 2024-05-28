from django.shortcuts import render, redirect
from . models import Login
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

# def login(request):
#     if request.method == 'POST':
#         form = LoginForm.POST()
#         if form.is_valid:
#             form.save()


def login_usuario(request):
    template_name = 'usuarios/login.html'
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            senha = form.cleaned_data['senha']
            user = authenticate(username=usuario, password=senha)
            if user is not None and user.is_active:
                login(request, user)
                messages.info(request, 'Você fez login com sucesso!')
                return redirect('geral:home')
            else:
                messages.error(request, 'Matrícula ou senha inválidos!')
                return redirect('usuarios:login')
            
        else:
            messages.error(request, 'Formulário Inválido!')
            return redirect('usuarios:login')
        
    form = LoginForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required
def sair(request):
    logout(request)
    return redirect('usuarios:login')           


@login_required
def alterar_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Sua senha foi alterada com sucesso!')
            return redirect('geral:home')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'usuarios/alterar_senha.html', {'form': form})
        
