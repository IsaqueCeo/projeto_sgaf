from django.db import models
from core.models import Empresa, Nivel, Disciplina, Aluno, SaladeAula
# Create your models here.

class Turma(models.Model):
    
    TIPO_TURMA = (
        ('A', 'Turma A'),
        ('B', 'Turma B'),
        ('C', 'Turma C'),
        ('D', 'Turma D'),
        ('E', 'Turma E'),
    )
    
    SERIE = (
        ('F11', '1º Ano'),
        ('F12', '2º Ano'),
        ('F13', '3º Ano'),
        ('F14', '4º Ano'),
        ('F15', '5º Ano'),
        ('F26', '6º Ano'),
        ('F27', '7º Ano'),
        ('F28', '8º Ano'),
        ('F29', '9º Ano'),
    )
    
    TURNO = (
        ('M', 'Matutino'),
        ('T', 'Vespertino'),
        ('N', 'Noturno'),
    )
    
    STATUS_CHOICES = (
        ('Iniciando', 'Iniciando'),
        ('Em andamento', 'Em andamento'),
        ('Férias', 'Férias'),
        ('Finalizada', 'Finalizada'),
        ('Suspensa', 'Suspensa'),
    )
    
    instituicao = models.ForeignKey(Empresa, verbose_name='Instituição', on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, verbose_name="Nível da Série")
    disciplinas = models.ManyToManyField(Disciplina, related_name='disciplinas', verbose_name="Disciplinas")
    ano_letivo = models.PositiveSmallIntegerField("Ano Letivo")
    nome_turma = models.CharField("Nome da Turma", choices=TIPO_TURMA, max_length=1)
    alunos = models.ManyToManyField(Aluno, related_name='alunos', verbose_name="Alunos")
    serie = models.CharField("Série da Turma", choices=SERIE, max_length=3)
    sala_de_aula = models.ForeignKey(SaladeAula, on_delete=models.CASCADE, verbose_name="Sala de Aula")
    turno = models.CharField("Turno da Turma", choices=TURNO, max_length=1)
    status = models.CharField("Status da Turma", max_length=20, choices=STATUS_CHOICES, default='Iniciando')


    def __str__(self):
        return f"Turma {self.nome_turma} -  {self.get_serie_display()}"
    
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"