from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class Usuario(AbstractUser):
    e_aluno = models.BooleanField(default=False)
    e_funcionario = models.BooleanField(default=False)
    
    
class Aluno(models.Model):
    matricula = models.CharField(max_length=20, unique=True, editable=False)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    curso = models.CharField(max_length=100)
    nome_responsavel = models.CharField(max_length=100)
    nome_social = models.CharField("Nome da Razão Social", max_length=100)
    ano_ingresso = models.DateTimeField(default=timezone.now().year)
    # data_nascimento = models.DateField(default=default_birth_date)
    # sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default=MASCULINO)
    

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



# class Aluno(models.Model):
#     ESTADO_CIVIL_CHOICES = [
#         ('solteiro', 'Solteiro'),
#         ('casado', 'Casado'),
#         ('divorciado', 'Divorciado'),
#         ('viuvo', 'Viúvo'),
#         ('outro', 'Outro'),
#     ]

#     UF_CHOICES = [
#         ('AC', 'Acre'),
#         ('AL', 'Alagoas'),
#         ('AP', 'Amapá'),
#         ('AM', 'Amazonas'),
#         ('BA', 'Bahia'),
#         ('CE', 'Ceará'),
#         ('DF', 'Distrito Federal'),
#         ('ES', 'Espírito Santo'),
#         ('GO', 'Goiás'),
#         ('MA', 'Maranhão'),
#         ('MT', 'Mato Grosso'),
#         ('MS', 'Mato Grosso do Sul'),
#         ('MG', 'Minas Gerais'),
#         ('PA', 'Pará'),
#         ('PB', 'Paraíba'),
#         ('PR', 'Paraná'),
#         ('PE', 'Pernambuco'),
#         ('PI', 'Piauí'),
#         ('RJ', 'Rio de Janeiro'),
#         ('RN', 'Rio Grande do Norte'),
#         ('RS', 'Rio Grande do Sul'),
#         ('RO', 'Rondônia'),
#         ('RR', 'Roraima'),
#         ('SC', 'Santa Catarina'),
#         ('SP', 'São Paulo'),
#         ('SE', 'Sergipe'),
#         ('TO', 'Tocantins'),
#     ]

#     estado_civil = models.CharField(
#         max_length=10,
#         choices=ESTADO_CIVIL_CHOICES,
#         default='solteiro',
#     )
#     religiao = models.CharField(max_length=100, blank=True)
#     uf_naturalidade = models.CharField(
#         max_length=2,
#         choices=UF_CHOICES,
#         blank=True,
#     )
#     naturalidade = models.CharField(max_length=100, blank=True)
#     nacionalidade = models.CharField(max_length=100, blank=True)

#     def __str__(self):
#         return f"{self.naturalidade} - {self.nacionalidade}"



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
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    endereco = models.CharField(max_length=100)
    formacao = models.CharField(max_length=100)
    