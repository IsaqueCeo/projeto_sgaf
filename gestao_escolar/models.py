from django.db import models
from core.models import Empresa, Nivel, Disciplina, Aluno, SaladeAula
from .utils import calcular_media_bimestre
# Create your models here.

class Serie(models.Model):
    SERIE = (
        ('F11', '1º Ano do Fundamental I'),
        ('F12', '2º Ano do Fundamental I'),
        ('F13', '3º Ano do Fundamental I'),
        ('F14', '4º Ano do Fundamental I'),
        ('F15', '5º Ano do Fundamental I'),
        ('F26', '6º Ano do Fundamental II'),
        ('F27', '7º Ano do Fundamental II'),
        ('F28', '8º Ano do Fundamental II'),
        ('F29', '9º Ano do Fundamental II'),
    )
    
    TURNO = (
        ('M', 'Matutino'),
        ('T', 'Vespertino'),
        ('N', 'Noturno'),
    )

    serie = models.CharField("Série da Turma", choices=SERIE, max_length=3)
    turno = models.CharField("Turno da Turma", choices=TURNO, max_length=1)

    def __str__(self):
        return f"{self.serie} -  {self.turno}"
    
    class Meta:
        verbose_name = "Série"
        verbose_name_plural = "Séries"


class Turma(models.Model):
    
    TIPO_TURMA = (
        ('A', 'Turma A'),
        ('B', 'Turma B'),
        ('C', 'Turma C'),
        ('D', 'Turma D'),
        ('E', 'Turma E'),
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
    sala_de_aula = models.ForeignKey(SaladeAula, on_delete=models.CASCADE, verbose_name="Sala de Aula")
    status = models.CharField("Status da Turma", max_length=20, choices=STATUS_CHOICES, default='Iniciando')
    serie = models.ForeignKey(Serie, related_name='series', verbose_name='series', on_delete=models.CASCADE)


    def __str__(self):
        return f"Turma {self.nome_turma} -  {self.get_serie_display()}"
    
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"
        
class Aula(models.Model):
    STATUS_AULA = (
        ('AG', 'Agendada'),
        ('EA', 'Em andamento'),
        ('CO', 'Concluída'),
        ('CA', 'Cancelada'),
    )

    data = models.DateField("Data da Aula")
    horario_inicio = models.TimeField("Horário de Início", blank=True, null=True)
    horario_termino = models.TimeField("Horário de Término", blank=True, null=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, verbose_name="Turma")
    conteudo = models.TextField("Conteúdo da Aula", blank=True, null=True)
    status = models.CharField("Status da Aula", max_length=10, choices=STATUS_AULA, default='SCHEDULED')

    def __str__(self):
        return f"Aula de {self.disciplina.nome} - {self.turma}"

    class Meta:
        verbose_name = "Aula"
        verbose_name_plural = "Aulas"
        
class FrequenciaDoAluno(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, verbose_name="Aula")
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, verbose_name="Aluno")
    presenca = models.BooleanField("Presença do Aluno", default=True)

    
    def __str__(self):
        return f"Frequência do {self.aluno.nome}"   

    class Meta:
        verbose_name = "Frequência do Aluno"
        verbose_name_plural = "Frequências do Aluno"
        

class BoletimDoAlunoPorDisciplina(models.Model):

    STATUS_APROVACAO = (
        ('APROVADO', 'Aprovado'),
        ('REPROVADO', 'Reprovado'),
        ('EM ANDAMENTO', 'Em Andamento'),
    )
    
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, verbose_name="Aluno")
    primeira_nota_bimestre_um = models.DecimalField("Nota da Prova 1", max_digits=5, decimal_places=2, blank=True, null=True)
    segunda_nota_bimestre_um = models.DecimalField("Nota da Prova 2", max_digits=5, decimal_places=2, blank=True, null=True)
    recuperacao_bimestre_um = models.DecimalField("Nota Recuperação do Bimestre 1", max_digits=5, decimal_places=2, blank=True, null=True)
    primeira_nota_bimestre_dois = models.DecimalField("Nota da Prova 3", max_digits=5, decimal_places=2, blank=True, null=True)
    segunda_nota_bimestre_dois = models.DecimalField("Nota da Prova 4", max_digits=5, decimal_places=2, blank=True, null=True)
    recuperacao_bimestre_dois = models.DecimalField("Nota Recuperação do Bimestre 2", max_digits=5, decimal_places=2, blank=True, null=True)
    primeira_nota_bimestre_tres = models.DecimalField("Nota da Prova 5", max_digits=5, decimal_places=2, blank=True, null=True)
    segunda_nota_bimestre_tres = models.DecimalField("Nota da Prova 6", max_digits=5, decimal_places=2, blank=True, null=True)
    recuperacao_bimestre_tres = models.DecimalField("Nota Recuperação do Bimestre 3", max_digits=5, decimal_places=2, blank=True, null=True)
    primeira_nota_bimestre_quatro = models.DecimalField("Nota da Prova 7", max_digits=5, decimal_places=2, blank=True, null=True)
    segunda_nota_bimestre_quatro = models.DecimalField("Nota da Prova 8", max_digits=5, decimal_places=2, blank=True, null=True)
    recuperacao_bimestre_quatro = models.DecimalField("Nota Recuperação do Bimestre 4", max_digits=5, decimal_places=2, blank=True, null=True)
    media_anual = models.DecimalField("Média Anual", max_digits=5, decimal_places=2, blank=True, null=True)
    prova_final = models.DecimalField("Prova Final do Anual", max_digits=5, decimal_places=2, blank=True, null=True)
    status_aprovacao = models.CharField("Status de Aprovação", max_length=15, choices=STATUS_APROVACAO, blank=True, null=True)
    
    def __str__(self):
        return f"Boletim de {self.aluno.nome} em {self.disciplina.nome}"
    
    @property
    def nota_media_bimestre_um(self):
        return calcular_media_bimestre(self.primeira_nota_bimestre_um, self.segunda_nota_bimestre_um)
    
    @property
    def nota_media_bimestre_dois(self):
        return calcular_media_bimestre(self.primeira_nota_bimestre_dois, self.segunda_nota_bimestre_dois)

    @property
    def nota_media_bimestre_tres(self):
        return calcular_media_bimestre(self.primeira_nota_bimestre_tres, self.segunda_nota_bimestre_tres)

    @property
    def nota_media_bimestre_quatro(self):
        return calcular_media_bimestre(self.primeira_nota_bimestre_quatro, self.segunda_nota_bimestre_quatro)
   
# class BoletimDoAluno(models.Model):
#     aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, verbose_name="Aluno")

#     @property
#     def disciplinas(self):
#         return BoletimDoAlunoPorDisciplina.objects.filter(aluno=self.aluno)   

