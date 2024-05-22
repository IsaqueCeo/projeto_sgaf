from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    e_aluno = models.BooleanField(default=False)
    e_funcionario = models.BooleanField(default=False)
    
    
class PerfilAluno(models.Model):
    matricula = models.CharField(max_length=20, unique=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    curso = models.CharField(max_length=100)
    nome_responsavel = models.CharField(max_length=100)
    ano_ingresso = models.PositiveIntegerField()

    def __str__(self):
        return self.usuario.username



class PerfilFuncionario(models.Model):
    matricula_funcionario = models.CharField(max_length=20, unique=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    departamento = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario.username