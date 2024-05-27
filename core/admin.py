from django.contrib import admin
from .models import Empresa, Setor, Funcionario, Aluno, Dadospessoais, Aluno, Nivel, SaladeAula, Disciplina, Professor
 
# Register your models here.

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ["id", "nome_fantasia", "cnpj", "email", "telefone", "cidade", "confirmado"]
    search_fields = ["nome_fantasia", "cnpj"]
    list_display_links = [ "nome_fantasia", "cnpj", "email", "telefone" ]
    list_per_page = 10
    list_editable = ["confirmado"]
    ordering = ['nome_fantasia', 'cidade']

@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    list_display = ["id", "empresa", "nome", "telefone"]
    list_display_links = [ "empresa", "nome"]
    search_fields = ["nome"]
    list_per_page = 10
    

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ["id", "empresa", "matricula", "nome", "cpf", "telefone", "email"]
    search_fields = ["nome", "matricula", "cpf"]
    list_display_links = ["id", "matricula", "nome"]
    list_per_page = 10

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ["id", "instituicao", "matricula", "nome", "cpf", "telefone", "email"]
    search_fields = ["nome", "matricula", "cpf"]
    list_display_links = ["id", "matricula", "nome"]
    list_per_page = 10
    ordering = ['nome', 'matricula']
    
@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ["id", "instituicao", "matricula", "nome", "cpf", "telefone", "email"]
    search_fields = ["nome", "matricula", "cpf"]
    list_display_links = ["id", "matricula", "nome"]
    list_per_page = 10
    ordering = ['nome', 'matricula']

@admin.register(Dadospessoais)
class DadospessoaisAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "cpf", "rg"]
    search_fields = ["nome", "cpf"]
    list_display_links = ["id", "nome", "cpf", "rg"]
    list_per_page = 10
    ordering = ['nome']

@admin.register(Nivel)
class NivelAdmin(admin.ModelAdmin):
    list_display = ["id", "nivel", ]
    list_per_page = 10
    list_display_links = ["id", "nivel"]
    
@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "carga_horaria", "professor", "ativo"]
    search_fields = ["nome", "carga_horaria"]
    list_editable = ["ativo"]
    list_display_links = ["id", "nome", "professor"]
    list_per_page = 10
     
@admin.register(SaladeAula)
class SalaDeAulaAdmin(admin.ModelAdmin):
    list_display = ["id", "numero", "andar", "acessibilidade", "estado_conservacao"]    
    list_per_page = 10
    list_display_links = ["id", "numero"]