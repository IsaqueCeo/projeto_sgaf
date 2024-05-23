from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    e_aluno = models.BooleanField(default=False)
    e_funcionario = models.BooleanField(default=False)
    
    
class Aluno(models.Model):
    matricula = models.CharField(max_length=20, unique=True, editable=False)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    curso = models.CharField(max_length=100)
    nome_responsavel = models.CharField(max_length=100)
    ano_ingresso = models.PositiveIntegerField()

    def gerar_matricula(self):
        if len(self.turma) >= 2:
            matricula = self.NIVEL[0][0] + self.turma[1]
        else:
            raise ValueError("A turma deve ter pelo menos 2 caracteres para gerar a matrícula.")
        return matricula

    def save(self, *args, **kwargs):
        if not self.matricula:
            while True:
                matricula = self.gerar_matricula()
                if not Aluno.objects.filter(matricula=matricula).exists():
                    self.matricula = matricula
                    break
        super().save(*args, **kwargs)
    
    
    # def __str__(self):
    #     return self.usuario.username



class Funcionario(models.Model):
    matricula_funcionario = models.CharField(max_length=20, unique=True, editable=False)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    departamento = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)

    def gerar_matricula(self):
        if len(self.departamento) >= 2:
            matricula =self.NIVEL[0][0] + self.departamento[1]
        else:
            raise ValueError("O departamento deve ter pelo menos 2 caracteres para gerar a matrícula.")
        return matricula

    def save(self, *args, **kwargs):
        if not self.matricula_funcionario:
            while True:
                matricula_funcionario = self.gerar_matricula()
                if not Funcionario.objects.filter(matricula=matricula_funcionario).exists():
                    self.matricula_funcionario = matricula_funcionario
                    break

        super().save(*args, **kwargs)




class Professor(models.Model):
    matricula_professor = models.CharField(max_length=100, unique=True, editable=False)
    cpf = models.BigIntegerField(unique=True)
    disciplina = models.ForeignKey()
    email = models.EmailField(unique=True)
    endereco = models.CharField(max_length=100)
    formacao = models.CharField(max_length=100)
    