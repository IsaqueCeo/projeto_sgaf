from django.urls import path
from .views import perfil_professor, atualizar_dados_pessoais_professor, listar_disciplinas_do_professor

urlpatterns = [
    path('', perfil_professor, name='perfil-professor'),
    path('atualizar-dados-pessoais/<int:id>/', atualizar_dados_pessoais_professor, name='atualizar-dados-pessoais-professor'),
    path('minhas-disciplinas/<int:id>', listar_disciplinas_do_professor, name='listar_disciplina_por_professor'),

]
