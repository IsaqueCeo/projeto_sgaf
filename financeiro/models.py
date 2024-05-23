from django.db import models
from django.utils import timezone
from Login.models import Aluno

class Pagamento(models.Model):
    PENDENTE = 'PENDENTE'
    PAGO = 'PAGO'
    ATRASADO = 'ATRASADO'
    CANCELADO = 'CANCELADO'

    STATUS_CHOICES = [
        (PENDENTE, PENDENTE),
        (PAGO, PAGO),
        (ATRASADO, ATRASADO),
        (CANCELADO, CANCELADO),
    ]

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateField(default=timezone.now)
    data_vencimento = models.DateField()
    data_pagamento = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices = STATUS_CHOICES,
        default = PENDENTE,
    )
    def __str__(self):
        return f'Pagamento {self.id} - Aluno: {self.aluno.nome}'
        # Verificar o nome do aluno se está criado

class Inadimplencia(models.Model):
    pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE)
    data_vencimento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f'Inadimplencia {self.id} - Pagamento: {self.pagamento.id}'

class HistoricoPagamento(models.Model):
    pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField()
    metodo_pagamento = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f'Histórico Pagamento {self.id} - Pagamento: {self.pagamento.id}'

class Fatura(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    valor_toral = models.DecimalField(max_digits=10, decimal_places=2)
    data_emissao = models.DateField(default=timezone.now)
    data_vencimento = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f'Fatura {self.id} - Aluno: {self.aluno.nome}'

class Desconto(models.Model):
    fatura = models.ForeignKey(Fatura, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_concessao = models.DateField(default=timezone.now)

    def __str__(self):
        return f'Desconto {self.id} - Fatura {self.fatura.id}'

class Taxa(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    frequencia = models.CharField(max_length=50)

    def __str__(self):
        return f'Taxa {self.id} - {self.nome}'

class PagamentoTaxa(models.Model):
    pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE)
    taxa = models.ForeignKey(Taxa, on_delete=models.CASCADE)

    def __str__(self):
        return f'Pagamento {self.pagamento.id} - Taxa {self.taxa.nome}'

class Multa(models.Model):
    pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_aplicacao = models.DateField(default=timezone.now)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f'Multa {self.id} - PAgamento {self.pagamento.id}'

class BolsaEstudo(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_concessao = models.DateField(default=timezone.now)

    def __str__(self):
        return f'Bolsa {self.id} - Aluno {self.aluno.nome}'

class Receita(models.Model):
    fonte = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_recebimento = models.DateField(default=timezone.now)
    descricao = models.TextField()

    def __str__(self):
        return f'Receita {self.id} - Fonte: {self.fonte}'

class Despesa(models.Model):
    tipo = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField(default=timezone.now)
    descricao = models.TextField()

    def __str__(self):
        return f'Despesa {self.id} - Tipo: {self.tipo}'

class Transacao(models.Model):
    tipo = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(default=timezone.now)
    descricao = models.TextField()
    relacionamento_id = models.IntegerField()
    relacionamento_tipo = models.CharField(max_length=50)

    def __str__(self):
        return f'Transacao {self.id} - Tipo: {self.tipo}'
