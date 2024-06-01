from django.urls import path
from .views import cadastrar_nova_serie, listar_series, atualizar_serie, deletar_serie, detalhar_serie
from .views import criar_turma, listar_turmas, atualizar_turma, deletar_turma, detalhar_turma
from .views import deletar_aula, atualizar_aula, detalhar_aula, listar_todas_aulas, cadastrar_nova_aula

urlpatterns = [
    path('nova-serie/', cadastrar_nova_serie, name='nova-serie'),
    path('listar-series/', listar_series, name='listar-series'),
    path('atualizar-serie/<int:id>/', atualizar_serie, name='atualizar-serie'),
    path('detalhar-serie/<int:id>/', detalhar_serie, name='detalhar-serie'),
    path('deletar-serie/<int:id>/', deletar_serie, name='deletar-serie'),
    
    path('nova-turma/', criar_turma, name='nova-turma'),
    path('listar-turmas/', listar_turmas, name='listar-turmas'),
    path('atualizar-turma/<int:id>/', atualizar_turma, name='atualizar-turma'),
    path('detalhar-turma/<int:id>/', detalhar_turma, name='detalhar-turma'),
    path('deletar-turma/<int:id>/', deletar_turma, name='deletar-turma'),
    
    path('nova-aula/', cadastrar_nova_aula, name='nova-aula'),
    path('listar-aulas/', listar_todas_aulas, name='listar-aulas'),
    path('atualizar-aula/<int:id>/', atualizar_aula, name='atualizar-aula'),
    path('detalhar-aula/<int:id>/', detalhar_aula, name='detalhar-aula'),
    path('deletar-aula/<int:id>/', deletar_aula, name='deletar-aula'),


]
