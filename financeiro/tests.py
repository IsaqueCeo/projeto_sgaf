from django.db import models
from django.core.validators import MinValueValidator

class Taxa(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    frequencia = models.CharField(max_length=50)  # Ex: Mensal, Anual

    def __str__(self):
        return self.nome

class Multa(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    data_aplicacao = models.DateField()
    status = models.CharField(max_length=50)  # Ex: Aplicada, Paga, Cancelada

class BolsaEstudo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

class BolsaEstudoAluno(models.Model):
    bolsa_estudo = models.ForeignKey(BolsaEstudo, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    data_concessao = models.DateField()

    class Meta:
        unique_together = ('bolsa_estudo', 'aluno')

class Fatura(models.Model):
    aluno = models.ForeignKey('core.Aluno', on_delete=models.CASCADE)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    data_emissao = models.DateField(auto_now_add=True)
    data_vencimento = models.DateField()
    status = models.CharField(max_length=50)  # Ex: Pendente, Paga, Atrasada

class Desconto(models.Model):
    fatura = models.ForeignKey(Fatura, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    data_concessao = models.DateField()

class Pagamento(models.Model):
    aluno = models.ForeignKey('core.Aluno', on_delete=models.CASCADE)
    fatura = models.ForeignKey(Fatura, on_delete=models.CASCADE)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    data_pagamento = models.DateField()
    metodo_pagamento = models.CharField(max_length=100)
    status = models.CharField(max_length=50)  # Ex: Completo, Parcial, Cancelado

class Inadimplencia(models.Model):
    aluno = models.ForeignKey('core.Aluno', on_delete=models.CASCADE)
    fatura = models.ForeignKey(Fatura, on_delete=models.CASCADE)
    data_vencimento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    status = models.CharField(max_length=50)  # Ex: Ativa, Paga

class HistoricoPagamento(models.Model):
    pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    data_pagamento = models.DateField()
    metodo_pagamento = models.CharField(max_length=100)
    status = models.CharField(max_length=50)  # Ex: Completo, Parcial, Cancelado

class PagamentoTaxa(models.Model):
    pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE)
    taxa = models.ForeignKey(Taxa, on_delete=models.CASCADE)

class Receita(models.Model):
    fonte = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    data_recebimento = models.DateField()
    descricao = models.TextField()

class Despesa(models.Model):
    tipo = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    data_pagamento = models.DateField()
    descricao = models.TextField()

class Transacao(models.Model):
    TIPO_CHOICES = [
        ('Receita', 'Receita'),
        ('Despesa', 'Despesa'),
    ]
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    data = models.DateField()
    descricao = models.TextField()
    relacionado_id = models.PositiveIntegerField()
    relacionado_tipo = models.CharField(max_length=100)