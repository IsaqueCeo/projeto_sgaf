from django.db import models
from django.db.models.signals import pre_save


# Create your models here.

class Empresa(models.Model):
    razao_social = models.CharField("Nome da Razão Social", max_length=50, blank=True, null=True)
    nome_fantasia = models.CharField("Nome da Fantasia da Empresa", max_length=50, blank=True, null=True)
    natureza_juridica = models.CharField("Natureza Jurídica da Empresa", max_length=70, blank=True, null=True)
    cnpj = models.CharField("CNPJ da Empresa", max_length=14)
    email = models.EmailField("Email da Empresa")
    telefone = models.CharField("Telefone da Empresa", max_length=11)
    cep = models.CharField("CEP da Empresa", max_length=8)
    endereco = models.CharField("Nome da Rua/Avenida", max_length=50, blank=True, null=True)
    bairro = models.CharField("Bairro", max_length=25, blank=True, null=True)
    cidade = models.CharField("Cidade", max_length=50, blank=True, null=True)
    estado = models.CharField("UF", max_length=2, blank=True, null=True)
    complemento = models.CharField("Complemento", max_length=50, blank=True, null=True)
    site = models.URLField("Site da Empresa", blank=True, null=True)
    codigo_inep = models.IntegerField("Código INEP da Instituição", blank=True, null=True)
    nome_diretor = models.CharField("Nome do Diretor(a) da Empresa", max_length=70, blank=True, null=True)
    assinatura_diretor = models.FileField("Assinatura do Diretor", blank=True, null=True)
    nome_secretario = models.CharField("Nome do Secretario(a) da Empresa", max_length=70, blank=True, null=True)
    assinatura_secretario = models.FileField("Assinatura do Secretário", blank=True, null=True)
    confirmado = models.BooleanField("Confirmar Dados", default=False)

    def __str__(self):
        return self.razao_social
    
    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

