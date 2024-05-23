from .models import Setor
from django.views.generic import CreateView
from .forms import NovoSetorForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

#View para criar um novo setor
class NovoSetor(LoginRequiredMixin, CreateView):
    model = Setor
    template_name = 'empresa/setor.html'
    form_class = NovoSetorForm
    
    def form_valid(self, form):
        form.instance.empresa = self.request.user.funcionario.empresa
        return super().form_valid(form)
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Setor criado com sucesso!")
        return reverse('home')
