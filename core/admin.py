from django.contrib import admin
from .models import Empresa, Setor, Funcionario, Aluno, Dadospessoais
 
# Register your models here.

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ["id", "nome_fantasia", "cnpj", "email", "telefone", "cidade", "confirmado"]
    search_fields = ["nome_fantasia", "cnpj"]
    list_per_page = 10
    list_editable = ["confirmado"]

@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    list_display = ["id", "empresa", "nome", "telefone"]
    search_fields = ["nome"]
    list_per_page = 10

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ["id", "empresa", "matricula", "nome", "cpf", "telefone", "email"]
    search_fields = ["nome", "matricula", "cpf"]
    list_per_page = 10

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ["id", "empresa", "matricula", "nome", "cpf", "telefone", "email"]
    search_fields = ["nome", "matricula", "cpf"]
    list_per_page = 10

@admin.register(Dadospessoais)
class DadospessoaisAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "cpf", "rg"]
    search_fields = ["nome", "cpf"]
    list_per_page = 10
