from django.db import models
from django.utils import timezone
from core.models import Aluno
from gestao_escolar.models import Serie


class Mensalidade(models.Model):    
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    valor = models.DecimalField('Valor da Mensalidade', decimal_places=2, max_digits=10)

    def __str__(self):

        return f'{self.serie} - {self.valor}'

class Taxa(models.Model):   




    juros = models.DecimalField('Juros', max_digits=3 ,decimal_places=2)
    multa = models.DecimalField('Multas', max_digits=3 ,decimal_places=2)



class Bolsa(models.Model):
    
    TIPO = (
        ('1','Percentual'),
        ('2', 'Valor Fixo')
    )
    
    valor_bolsa = models.DecimalField('Bolsa', max_digits=6, decimal_places=2 )
    tipo = models.CharField('Tipo da Bolsa', max_length=50 ,choices=TIPO)

    def __str__(self):
        if self.tipo == '1':
            return f'O valor da bolsa é de {self.valor_bolsa}%'
        else:
            return f'O valor da bolsa é de R${self.valor_bolsa}'



class Fatura(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    valor_mensal = models.ForeignKey(Mensalidade, on_delete=models.CASCADE)
    data_emissao = models.DateField(default=timezone.now)
    data_vencimento = models.DateField()
    status = models.CharField(max_length=50)
    bolsa = models.ForeignKey(Bolsa, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Fatura {self.id} - Aluno: {self.aluno.nome}'
    
class Pagamento(models.Model):

    STATUS = (
        ('1', 'Pendente'),
        ('2', 'Atrasado'),
        ('3', 'Pago'),
    )


    boleto = models.ForeignKey(Fatura, on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)
    status = models.CharField('Status',max_length=50 , choices=STATUS)

class Despesa(models.Model):

    CATEGORIA = (
        ('1','Salário'),
        ('2','Compra de Material'),
        ('3','Infraestrutura'),
        ('4','Serviços Terceirizados'),
        ('5','Manutenção'),
        ('6','Outros'),
    )

    nome = models.CharField('Nome da Despesa', max_length=150, blank=False, null=False)
    categoria = models.CharField('Categoria da Despesa',max_length=50,choices=CATEGORIA)
    valor = models.DecimalField('Valor',decimal_places=2, max_digits=5)
    data  = models.DateField('Data do Pagamento', auto_now_add=True)
    descricao = models.TextField('Descrição do Pagamento', max_length=300, blank=True)
    metodo = models.CharField('Método de Pagamento',max_length=50 ,blank=True)


class Faturamento(models.Model):
    CATEGORIA = (
        ('1','Mensalidade'),
        ('2','Pagamentos Externos'),
        ('3','Vendas'),
        ('4','Livros'),
        ('5','Atividades Complementares'),
        ('6','Outros'),
    )

    nome = models.CharField('Nome do Faturamento', max_length=150, blank=False, null=False)
    categoria = models.CharField('Categoria do Faturamento',max_length=50,choices=CATEGORIA)
    valor = models.DecimalField('Valor',decimal_places=2, max_digits=5)
    data  = models.DateField('Data do Fautramento', auto_now_add=True)
    descricao = models.TextField('Descrição do Faturamento', max_length=300, blank=True)



    









