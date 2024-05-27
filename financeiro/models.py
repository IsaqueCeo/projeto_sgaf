from django.db import models
from django.utils import timezone
from core.models import Aluno
from gestao_escolar.models import Serie

class Mensalidade(models.Model):
    
    serie = models.ForeignKey(Serie)
    valor = models.FloatField()


