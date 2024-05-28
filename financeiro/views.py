from django.shortcuts import render, redirect, get_object_or_404
from models import Faturamento, Fatura, Despesa, Mensalidade, Pagamento, Taxa
from django.contrib.auth.decorators import login_required
from forms import FaturaForm, FaturamentoForm, DespesaForm, MensalidadeForm, PagamentoForm, TaxaForm

# Create your views here.

@login_required
def NovaMensalidade(request):

    template_name = ''
    context = {

    } 

    return render(request, template_name, context)

@login_required
def EditarMensalidade(request, pk):

    template_name = ''
    context = {
    }
    mensalidade = get_object_or_404(Mensalidade, pk=pk)
    if request.method == 'POST':
       form = MensalidadeForm(data=request.POST, instance=mensalidade)
       form.save()
    form = MensalidadeForm(instance=mensalidade)
    context['form'] = form
    return render(request, template_name, context)

@login_required

def NovaTaxa(request, pk):

    template_name = ''
    context = {

    }
    taxa = get_object_or_404

        
