from django.db import models
from django.utils import timezone
from .models import login

class Pagamentos(models.Model):
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

    aluno = models.ForeignKey(login, on_delete=models.CASCADE)
    valor_toal = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateField(default=timezone.now)
    data_vencimento = models.DateField()
    data_pagamento = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices = STATUS_CHOICES,
        default = PENDENTE,
    )



# Create your models here.
