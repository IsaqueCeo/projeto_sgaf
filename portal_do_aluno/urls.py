from django.urls import path
from .views import atualizar_dados_pessoais_aluno, listar_disciplinas_aluno, consultar_minhas_notas_por_disciplina, perfil_aluno

urlpatterns = [
    path('', perfil_aluno, name='perfil-aluno'),
    path('atualizar-dados-pessoais/<int:id>/', atualizar_dados_pessoais_aluno, name='atualizar-dados-pessoais-aluno'),
    path('minhas-disciplinas/<int:id>/', listar_disciplinas_aluno, name='minhas-disciplinas'),
    path('minhas-disciplinas/<int:id>/consultar-notas/<int:id_disciplina>', consultar_minhas_notas_por_disciplina, name='minhas-notas-por-disciplinas'),
    
]
