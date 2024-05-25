from django.contrib import admin
from .models import Turma

# Register your models here.
@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ["id", "instituicao", "sala_de_aula", "turno", "status"]
    search_fields = ["id", "sala_de_aula"]
    list_editable = ["status"]
    list_per_page = 10