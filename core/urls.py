from django.urls import path
from .views import novo_setor, listar_setores, atualizar_setor, deletar_setor, detalhar_setor, cadastrar_empresa_adm, listar_empresas_cadastradas, atualizar_empresa_cadastrada, detalhar_empresa_cadastrada, deletar_empresa_cadastrada
from .views import novo_professor, listar_professores, atualizar_professor, deletar_professor, detalhar_professor
from .views import novo_funcionario, listar_funcionarios, atualizar_funcionario, deletar_funcionario, detalhar_funcionario
from .views import deletar_aluno, atualizar_aluno, detalhar_aluno, listar_alunos, criar_aluno, desativar_disciplina, ativar_disciplina, marcar_sala_como_acessivel, marcar_sala_como_inacessivel
from .views import deletar_disciplina, atualizar_disciplina, detalhar_disciplina, listar_disciplinas, criar_disciplina
from .views import criar_sala_de_aula, listar_salas_de_aula, deletar_sala_de_aula, detalhar_sala_de_aula, atualizar_sala_de_aula

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
    
    path('cadastrar-aluno/', criar_aluno, name='cadastrar-aluno-na-empresa'),
    path('listar-alunos/', listar_alunos, name='listar-alunos'),
    path('atualizar-aluno/<int:id>/', atualizar_aluno, name='atualizar-aluno'),
    path('detalhar-aluno/<int:id>/', detalhar_aluno, name='detalhar-aluno'),
    path('deletar-aluno/<int:id>/', deletar_aluno, name='deletar-aluno'),
    
    path('cadastrar-disciplina/', criar_disciplina, name='cadastrar-disciplina-na-empresa'),
    path('listar-disciplinas/', listar_disciplinas, name='listar-disciplinas'),
    path('atualizar-disciplina/<int:id>/', atualizar_disciplina, name='atualizar-disciplina'),
    path('detalhar-disciplina/<int:id>/', detalhar_disciplina, name='detalhar-disciplina'),
    path('deletar-disciplina/<int:id>/', deletar_disciplina, name='deletar-disciplina'),
    path('detalhar-disciplina/<int:id>/ativar/', ativar_disciplina, name='ativar-disciplina'),
    path('detalhar-disciplina/<int:id>/desativar/', desativar_disciplina, name='deativar-disciplina'),
    
    path('cadastrar-sala-de-aula/', criar_sala_de_aula, name='nova-sala-de-aula'),
    path('listar-salas-de-aula/', listar_salas_de_aula, name='listar-salas-de-aula'),
    path('deletar-sala-de-aula/<int:id>/', deletar_sala_de_aula, name='deletar-sala-de-aula'),
    path('detalhar-sala-de-aula/<int:id>/', detalhar_sala_de_aula, name='detalhar-sala-de-aula'),
    path('atualizar-sala-de-aula/<int:id>/', atualizar_sala_de_aula, name='atualizar-sala-de-aula'),
    path('detalhar-sala-de-aula/<int:id>/sem-acessibilidade/', marcar_sala_como_inacessivel, name='sala-sem-acessibilidade'),
    path('detalhar-sala-de-aula/<int:id>/com-acessibilidade/', marcar_sala_como_acessivel, name='sala-com-acessibilidade'),

]
