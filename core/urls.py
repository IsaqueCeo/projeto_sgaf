from django.urls import path
from .views import novo_setor, listar_setores, atualizar_setor, deletar_setor, detalhar_setor, cadastrar_empresa_adm, listar_empresas_cadastradas, atualizar_empresa_cadastrada, detalhar_empresa_cadastrada, deletar_empresa_cadastrada
from .views import novo_professor, listar_professores, atualizar_professor, deletar_professor, detalhar_professor
from .views import novo_funcionario, listar_funcionarios, atualizar_funcionario, deletar_funcionario, detalhar_funcionario


urlpatterns = [
    path('novo-setor/', novo_setor, name='novo-setor'),
    path('listar-setores/', listar_setores, name='listar-setores'),
    path('atualizar-setor/<int:id>/', atualizar_setor, name='atualizar-setor'),
    path('detalhar-setor/<int:id>/', detalhar_setor, name='detalhar-setor'),
    path('deletar-setor/<int:id>/', deletar_setor, name='deletar-setor'),
    
    path('cadastrar-empresa/', cadastrar_empresa_adm, name='cadastrar-empresa'),
    path('listar-empresas-cadastradas/', listar_empresas_cadastradas, name='listar-empresas-cadastradas'),
    path('atualizar-empresa-cadastrada/<int:id>/', atualizar_empresa_cadastrada, name='atualizar-empresa-cadastrada'),
    path('detalhar-empresa-cadastrada/<int:id>/', detalhar_empresa_cadastrada, name='detalhar-empresa-cadastrada'),
    path('deletar-empresa-cadastrada/<int:id>/', deletar_empresa_cadastrada, name='deletar-empresa-cadastrada'),

    path('cadastrar-professor/', novo_professor, name='cadastrar-professor-na-empresa'),
    path('listar-professores/', listar_professores, name='listar-professores-da-empresa'),
    path('atualizar-professor/<int:id>/', atualizar_professor, name='atualizar-professor'),
    path('detalhar-professor/<int:id>/', detalhar_professor, name='detalhar-professor'),
    path('deletar-professor/<int:id>/', deletar_professor, name='deletar-professor'),
    
    path('cadastrar-funcionario/', novo_funcionario, name='cadastrar-funcionario-na-empresa'),
    path('listar-funcionarios/', listar_funcionarios, name='listar-funcionarios-da-empresa'),
    path('atualizar-funcionario/<int:id>/', atualizar_funcionario, name='atualizar-funcionario'),
    path('detalhar-funcionario/<int:id>/', detalhar_funcionario, name='detalhar-funcionario'),
    path('deletar-funcionario/<int:id>/', deletar_funcionario, name='deletar-funcionario'),

]
