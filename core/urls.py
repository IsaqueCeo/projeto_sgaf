from django.urls import path
from .views import novo_setor, listar_setores, atualizar_setor, deletar_setor, detalhar_setor, cadastrar_empresa_adm


urlpatterns = [
    path('novo-setor/', novo_setor, name='novo-setor'),
    path('listar-setores/', listar_setores, name='listar-setores'),
    path('atualizar-setor/<int:id>/', atualizar_setor, name='atualizar-setor'),
    path('detalhar-setor/<int:id>/', detalhar_setor, name='detalhar-setor'),
    path('deletar-setor/<int:id>/', deletar_setor, name='deletar-setor'),
    
    path('cadastrar-empresa/', cadastrar_empresa_adm, name='cadastrar-empresa'),

]
