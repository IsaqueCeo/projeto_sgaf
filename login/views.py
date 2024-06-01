from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from rolepermissions.decorators  import has_permission_decorator

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
                
                if hasattr(user, 'aluno'):
                    return redirect('perfil_aluno')
                elif hasattr(user, 'funcionario'):
                    return redirect('dashboard_empresa')
                elif hasattr(user, 'professor'):
                    return redirect('perfil_professor')
                else:
                    messages.error(request, 'Usuário não possui um perfil associado.')
                    return redirect('login')

            else:
                messages.error(request, 'Matrícula ou senha inválidos!')
                return redirect('login')
        else:
            messages.error(request, 'Formulário Inválido!')
            return redirect('login')
        
    form = LoginForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required
@has_permission_decorator('sair') 
def sair(request):
    logout(request)
    return redirect('usuarios:login')           


@login_required
@has_permission_decorator('alterar_senha') 
def alterar_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Sua senha foi alterada com sucesso!')
            if hasattr(user, 'aluno'):
                return redirect('perfil_aluno')
            elif hasattr(user, 'funcionario'):
                return redirect('dashboard_empresa')
            elif hasattr(user, 'professor'):
                return redirect('perfil_professor')
            else:
                messages.error(request, 'Usuário não possui um perfil associado.')
                return redirect('login')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'usuarios/alterar_senha.html', {'form': form})
        
