from django.contrib import admin
from .models import Turma, Aula, Serie ,FrequenciaDoAluno

# Register your models here.
@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ["id", "instituicao",  "nome_turma" ,"sala_de_aula", "status"]
    list_display_links = ["id", "nome_turma"]
    search_fields = ["id", "sala_de_aula"]
    list_editable = ["status"]
    list_per_page = 10
    
    
@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ["id", "data", "disciplina", "turma", "status"]
    list_display_links = ["id", "data", "disciplina", ]
    search_fields = ["data", "disciplina"]
    list_editable = ["status"]
    list_per_page = 10

admin.site.register(Serie)

    
@admin.register(FrequenciaDoAluno)
class FrequenciaDoAlunoAdmin(admin.ModelAdmin):
    list_display = ["id", "aula", "aluno", "presenca"]
    list_display_links = ["id", "aula", "aluno"]
    list_editable = ["presenca"]
    list_per_page = 10