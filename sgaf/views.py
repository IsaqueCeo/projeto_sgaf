from django.shortcuts import render, redirect
from core.forms import LandingPageEmpresaForm
from django.contrib import messages


def home(request):
    template_name = 'home.html'
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

