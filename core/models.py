from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User


# Create your models here.

class Dadospessoais(models.Model):

    
    ESTADO_CIVIL = (
        ('S', 'Solteiro(a)'),
        ('C', 'Casado(a)'),
        ('V', 'Viúvo(a)'),
        ('D', 'Divorciado(a)'),
        ('U', 'União Estável'),
    )
    
    
    RELIGIAO = (
        ('AS', 'Adventista do Sétimo Dia'),
        ('AG', 'Agnóstico'),
        ('BU', 'Budismo'),
        ('CA', 'Candomblé'),
        ('CR', 'Católicismo'),
        ('ES', 'Espiritismo'),
        ('EV', 'Evangélico'),
        ('HI', 'Hinduísmo'),
        ('IS', 'Islamismo'),
        ('JU', 'Judaísmo'),
        ('TJ', 'Testemunha de Jeová'),
        ('UM', 'Umbanda'),
        ('SR', 'Sem Religião'),
    )
        
    ESTADO = (
		('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'),
		('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
		('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'),
		('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
		('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'),
		('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'),
		('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
		('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'),
		('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'),
		('TO', 'Tocantins')
	)
    
    ORGAOS_EXPEDIDORES = [
        ('SSP', 'Secretaria de Segurança Pública'),
        ('PC', 'Polícia Civil'),
        ('DETRAN', 'Departamento de Trânsito'),
        ('ITEP', 'Instituto Técnico-Científico de Perícia'),
        ('POLITEC', 'Politec'),
        ('IGP', 'Instituto-Geral de Perícias'),
        ('IPC', 'Instituto de Polícia Científica'),
    ]
    

    nome = models.CharField("Nome Completo", max_length=100)    
    data_nascimento = models.DateField('Data de Nascimento')    
    uf_naturalizado = models.CharField('Estado', max_length=2, choices=ESTADO)
    estado_civil = models.CharField("Estado Civil", max_length=1, choices=ESTADO_CIVIL, null=True, blank=True)
    religiao = models.CharField("Religião", max_length=2, choices=RELIGIAO, null=True, blank=True)
    cep = models.CharField("CEP", max_length=8)
    uf = models.CharField("UF", max_length=2, choices=ESTADO)
    cidade = models.CharField('Cidade', max_length=50)
    endereco = models.CharField("Nome da Rua/Avenida", max_length=50)
    bairro = models.CharField("Bairro", max_length=25)
    numero = models.CharField("Número", max_length=25)
    nacionalidade = models.CharField("Nacionalidade", max_length=20, default="Brasileira")
    cpf = models.CharField("CPF", max_length=11, unique=True)
    rg = models.CharField("RG", max_length=20, unique=True)
    rg_frente_digitalizado = models.FileField("RG Frente Digitalizado", upload_to='documentos/rg/%Y/%m/%d/', null=True, blank=True)
    rg_verso_digitalizado = models.FileField("RG Verso Digitalizado", upload_to='documentos/rg/%Y/%m/%d/', null=True, blank=True)
    cpf_digitalizado = models.FileField("CPF Digitalizado", upload_to='documentos/cpf/%Y/%m/%d/', null=True, blank=True)
    certidao_nascimento_digitalizado = models.FileField("Certidão de Nascimento Digitalizada", upload_to='documentos/certidao/%Y/%m/%d/', null=True, blank=True)
    orgao_expedidor = models.CharField("Órgão Expedidor", max_length=20, choices=ORGAOS_EXPEDIDORES, null=True, blank=True)
    uf_orgao_expedidor = models.CharField('UF do Órgão Expedidor', max_length=2, choices=ESTADO, null=True, blank=True)
    nis = models.CharField('Número de Identificação Social', max_length=15, null=True, blank=True)
    numero_do_titulo = models.CharField('Número do Título de Eleitor', max_length=2, null=True, blank=True)
    numero_da_zona = models.CharField('Número da Zona Eleitoral', max_length=10, null=True, blank=True)
    numero_da_secao = models.CharField('Número da Seção Eleitoral', max_length=10, null=True, blank=True)
    
    def __str__(self):
        return f"Dados Pessoais de {self.nome}"
    
    class Meta:
        verbose_name = "Dado Pessoal"
        verbose_name_plural = "Dados Pessoais"  

class Empresa(models.Model):
    usuario = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.CASCADE, blank=True, null=True)
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


class Setor(models.Model):
    empresa = models.ForeignKey(Empresa, verbose_name='Empresa', on_delete=models.CASCADE)
    nome = models.CharField("Nome do Setor", max_length=100)
    telefone = models.CharField("Telefone do setor", max_length=11)
    observacoes = models.TextField("Atribuições do Setor", default="Setor da empresa em alta produtividade")
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Setor"
        verbose_name_plural = "Setores"  
