from django.shortcuts import render, redirect
from core.forms import LandingPageEmpresaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators  import has_permission_decorator


def home(request):
    template_name = 'index.html'
    if request.method == 'POST':
        form = LandingPageEmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Setor criado com sucesso!")
            return redirect('home')
    else:
        form = LandingPageEmpresaForm(request.POST)
    context = {'form': form}
    return render(request, template_name, context)

@login_required
@has_permission_decorator('dashboard') 
def dashboard(request):
    template_name = 'empresa/dashboard.html'
    context = {}
    return render(request, template_name, context)
    