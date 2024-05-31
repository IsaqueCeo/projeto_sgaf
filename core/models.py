from django.db import models
from django.db.models.signals import pre_save
import string
from django.contrib.auth.models import User
import random, re
from django.utils import timezone
from datetime import date
from validate_docbr import CPF, CNPJ
from django.core.exceptions import ValidationError


# Create your models here.

class Dadospessoais(models.Model):

    
    ESTADO_CIVIL = (
        ('S', 'Solteiro(a)'),
        ('C', 'Casado(a)'),
        ('V', 'Viúvo(a)'),
        ('D', 'Divorciado(a)'),
        ('U', 'União Estável'),
    )
    
    TIPO_SANGUINEO = (
        ('A-', 'A-'),
        ('A+', 'A+'),
        ('B-', 'B-'),
        ('B+', 'B+'),
        ('AB-', 'AB-'),
        ('AB+', 'AB+'),
        ('O-', 'O-'),
        ('O+', 'O+'),
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
    nome_da_mae = models.CharField("Nome da Mãe", max_length=100, null=True, blank=True)  
    nome_do_pai = models.CharField("Nome do Pai", max_length=100, null=True, blank=True)  
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
    passaporte = models.CharField('Número do Passaporte', max_length=10, blank=True, null=True)
    fator_sanguineo = models.CharField("Fator Sanguíneo", max_length=5, choices=TIPO_SANGUINEO, null=True, blank=True)
    peso = models.DecimalField('Peso', max_digits=5, decimal_places=2, blank=True, null=True)
    altura = models.DecimalField('Altura', max_digits=4, decimal_places=2, blank=True, null=True)
    convenio_medico = models.CharField('Convênio Médico', max_length=100, blank=True, null=True)
    informacoes_saude = models.TextField('Outras Informações', blank=True, null=True)
    telefone_emergencia = models.CharField('Telefone de Emergência', max_length=15, blank=True, null=True)
    alergias = models.TextField('Alergias', blank=True, null=True)
    restricoes_alimentares = models.TextField('Restrições Alimentares', blank=True, null=True)
    doencas = models.TextField('Doenças', blank=True, null=True)
    deficiencias = models.TextField('Transtornos/Deficiências', blank=True, null=True)
    laudos = models.FileField('Laudos', upload_to='documentos/laudos/%Y/%m/%d/', blank=True, null=True)
    vacinas = models.TextField('Vacinas', blank=True, null=True)
    medicamentos = models.TextField('Medicamentos', blank=True, null=True)
    
    def __str__(self):
        return f"Dados Pessoais de {self.nome}"
    
    class Meta:
        verbose_name = "Dado Pessoal"
        verbose_name_plural = "Dados Pessoais"  

class Empresa(models.Model):
    usuario = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE, blank=True, null=True)
    razao_social = models.CharField("Nome da Razão Social", max_length=50, blank=True, null=True)
    nome_fantasia = models.CharField("Nome Fantasia", max_length=50, blank=True, null=True)
    natureza_juridica = models.CharField("Natureza Jurídica", max_length=70, blank=True, null=True)
    cnpj = models.CharField("CNPJ", max_length=18, unique=True) 
    email = models.EmailField("Email")
    telefone = models.CharField("Telefone", max_length=11)
    cep = models.CharField("CEP", max_length=8)
    endereco = models.CharField("Endereço", max_length=50, blank=True, null=True)
    bairro = models.CharField("Bairro", max_length=25, blank=True, null=True)
    cidade = models.CharField("Cidade", max_length=50, blank=True, null=True)
    estado = models.CharField("UF", max_length=2, blank=True, null=True)
    complemento = models.CharField("Complemento", max_length=50, blank=True, null=True)
    site = models.URLField("Site", blank=True, null=True)
    codigo_inep = models.IntegerField("Código INEP", blank=True, null=True)
    nome_diretor = models.CharField("Nome do Diretor(a)", max_length=70, blank=True, null=True)
    assinatura_diretor = models.FileField("Assinatura do Diretor", blank=True, null=True, upload_to='assinaturas/')
    nome_secretario = models.CharField("Nome do Secretário(a)", max_length=70, blank=True, null=True)
    assinatura_secretario = models.FileField("Assinatura do Secretário", blank=True, null=True, upload_to='assinaturas/')
    confirmado = models.BooleanField("Confirmar Dados", default=False)

    def __str__(self):
        return self.razao_social

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def validate_cnpj(self):
        self.cnpj = re.sub(r'\D', '', self.cnpj)
        cnpj = CNPJ()
        if not cnpj.validate(self.cnpj):
            raise ValidationError('CNPJ inválido!')

    def save(self, *args, **kwargs):
        self.validate_cnpj()
        super().save(*args, **kwargs)


class Setor(models.Model):
    empresa = models.ForeignKey(Empresa, verbose_name='Empresa', on_delete=models.CASCADE)
    nome = models.CharField("Nome do Setor", max_length=100)
    telefone = models.CharField("Telefone do Setor", max_length=11)
    observacoes = models.TextField("Atribuições do Setor", default="Setor da empresa em alta produtividade")
    codigo = models.CharField("Código", max_length=5, unique=True, editable=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Setor"
        verbose_name_plural = "Setores"

    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = self.generate_unique_code()
        super().save(*args, **kwargs)

    def generate_unique_code(self):
        prefix = (self.nome[:2] + self.nome.split()[1][:2]).upper() if len(self.nome.split()) > 1 else self.nome[:2].upper()
        suffix = ''.join(random.choices(string.digits, k=3))
        code = prefix + suffix

        while Setor.objects.filter(codigo=code).exists():
            suffix = ''.join(random.choices(string.digits, k=3))
            code = prefix + suffix

        return code


class Professor(models.Model):
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
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
    
    instituicao = models.ForeignKey(Empresa, verbose_name='Instituição', on_delete=models.CASCADE, blank=True, null=True)
    usuario = models.OneToOneField(User, verbose_name="Usuario", on_delete=models.CASCADE, blank=True, null=True)
    dados_pessoais = models.OneToOneField(Dadospessoais, verbose_name='Dados Pessoais', blank=True, null=True, on_delete=models.SET_NULL)
    telefone = models.CharField("Telefone", max_length=11)
    nome = models.CharField("Nome Completo", max_length=100)
    nome_da_mae = models.CharField("Nome da Mãe", max_length=100, default='Nome da Mãe')
    nome_do_pai = models.CharField("Nome do Pai", max_length=100, blank=True, null=True)
    sexo = models.CharField("Sexo", max_length=1, choices=SEXO)
    uf_naturalizado = models.CharField('Estado', max_length=2, choices=ESTADO)
    cpf = models.CharField("CPF", max_length=14, unique=True)
    rg = models.CharField("RG", max_length=20, unique=True)
    cep = models.CharField("CEP", max_length=8)
    uf = models.CharField("UF", max_length=2, choices=ESTADO)
    cidade = models.CharField('Cidade', max_length=50)
    endereco = models.CharField("Nome da Rua/Avenida", max_length=50)
    bairro = models.CharField("Bairro", max_length=25)
    numero = models.CharField("Número", max_length=25)
    complemento = models.CharField("Complemento", max_length=20, blank=True, null=True)
    nacionalidade = models.CharField("Nacionalidade", max_length=20, default="Brasileira")
    data_nascimento = models.DateField('Data de Nascimento')
    email = models.EmailField("Email")
    matricula = models.CharField(max_length=20, unique=True, editable=False)   
    ano_ingresso = models.DateTimeField(default=timezone.now)


    @property
    def idade(self):
        hoje = date.today()
        diferenca = hoje - self.data_nascimento
        return round(diferenca.days // 365.25)
    
    def __str__(self):
        return self.nome
    
    
    def gerar_matricula(self):
        ano_ingresso = str(self.ano_ingresso.year)
        setor_abreviado = self.nome[:3].upper()
        numeros_aleatorios = ''.join(random.choices('0123456789', k=4))
        nome_abreviado = self.nome[:2].upper()
        self.matricula = ano_ingresso + setor_abreviado + numeros_aleatorios + nome_abreviado
        return self.matricula
    
    
    def validate_cpf(self):
        self.cpf = re.sub(r'\D', '', self.cpf)
        cpf = CPF()
        if not cpf.validate(self.cpf):
            raise ValidationError(f'CPF inválido!')
        

    def save(self, *args, **kwargs):
        if not self.matricula:
            self.gerar_matricula()
        self.validate_cpf()
        super().save(*args, **kwargs)
    
    
    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professores" 

class Funcionario(models.Model):
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
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
        
    usuario = models.OneToOneField(User, verbose_name='Usuario', on_delete=models.CASCADE, blank=True, null=True, related_name='funcionario')
    empresa = models.ForeignKey(Empresa, verbose_name='Empresa', on_delete=models.CASCADE, blank=True, null=True)
    dados_pessoais = models.OneToOneField(Dadospessoais, verbose_name='Dados Pessoais', blank=True, null=True, related_name='funcionario', on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    telefone = models.CharField("Telefone", max_length=11)
    nome = models.CharField("Nome Completo", max_length=100)
    nome_da_mae = models.CharField("Nome da Mãe", max_length=100, default='Nome da Mãe')
    nome_do_pai = models.CharField("Nome do Pai", max_length=100, blank=True, null=True)
    sexo = models.CharField("Sexo", max_length=1, choices=SEXO)
    uf_naturalizado = models.CharField('Estado', max_length=2, choices=ESTADO)
    cpf = models.CharField("CPF", max_length=14, unique=True)
    rg = models.CharField("RG", max_length=20, unique=True)
    cep = models.CharField("CEP", max_length=8)
    uf = models.CharField("UF", max_length=2, choices=ESTADO)
    cidade = models.CharField('Cidade', max_length=50)
    endereco = models.CharField("Nome da Rua/Avenida", max_length=50)
    bairro = models.CharField("Bairro", max_length=25)
    numero = models.CharField("Número", max_length=25)
    nacionalidade = models.CharField("Nacionalidade", max_length=20, default="Brasileira")
    data_nascimento = models.DateField('Data de Nascimento')
    email = models.EmailField("Email")
    matricula = models.CharField("Matrícula", max_length=20, unique=True, editable=False)    
    data_de_ingresso = models.DateTimeField(default=timezone.now)
    
    @property
    def idade(self):
        hoje = date.today()
        diferenca = hoje - self.data_nascimento
        return round(diferenca.days // 365.25) 

    def __str__(self):
        return self.nome
    
    def gerar_matricula(self):
        ano_ingresso = str(self.ano_ingresso.year)
        setor_abreviado = self.setor.nome[:3].upper()
        nome_abreviado = self.nome[:2].upper()
        
        while True:
            numeros_aleatorios = ''.join(random.choices('0123456789', k=3))
            matricula = ano_ingresso + setor_abreviado + numeros_aleatorios + nome_abreviado
            if not Funcionario.objects.filter(matricula=matricula).exists():
                break
        
        self.matricula = matricula

    def validate_cpf(self):
        self.cpf = re.sub(r'\D', '', self.cpf)
        cpf = CPF()
        if not cpf.validate(self.cpf):
            raise ValidationError(f'CPF inválido!')

    def save(self, *args, **kwargs):
        if not self.matricula:
            self.gerar_matricula()
        self.validate_cpf()
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"  


class Aluno(models.Model):
    

    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
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
    
    instituicao = models.ForeignKey(Empresa, verbose_name='Instituição', on_delete=models.CASCADE, blank=True, null=True)
    usuario = models.OneToOneField(User, verbose_name="Usuario", on_delete=models.CASCADE, blank=True, null=True)
    dados_pessoais = models.OneToOneField(Dadospessoais, verbose_name='Dados Pessoais', blank=True, null=True, on_delete=models.SET_NULL)
    telefone = models.CharField("Telefone", max_length=11)
    nome = models.CharField("Nome Completo", max_length=100)
    nome_da_mae = models.CharField("Nome da Mãe", max_length=100)
    nome_do_pai = models.CharField("Nome do Pai", max_length=100, blank=True, null=True)
    sexo = models.CharField("Sexo", max_length=1, choices=SEXO)
    uf_naturalizado = models.CharField('Estado de Nascimento', max_length=2, choices=ESTADO)
    cpf = models.CharField("CPF", max_length=14, unique=True)
    rg = models.CharField("RG", max_length=20, unique=True)
    cep = models.CharField("CEP", max_length=8)
    uf = models.CharField("UF de Residência", max_length=2, choices=ESTADO)
    cidade = models.CharField('Cidade', max_length=50)
    endereco = models.CharField("Nome da Rua/Avenida", max_length=50)
    bairro = models.CharField("Bairro", max_length=25)
    numero = models.CharField("Número", max_length=25)
    complemento = models.CharField("Complemento", max_length=20, blank=True, null=True)
    nacionalidade = models.CharField("Nacionalidade", max_length=20, default="Brasileira")
    data_nascimento = models.DateField('Data de Nascimento')
    email = models.EmailField("Email")
    matricula = models.CharField(max_length=20, unique=True, editable=False)       
    data_de_ingresso = models.DateTimeField(default=timezone.now)



    @property
    def idade(self):
        hoje = date.today()
        diferenca = hoje - self.data_nascimento
        return round(diferenca.days // 365.25)
    
    def __str__(self):
        return self.nome
    
    
    def gerar_matricula(self):
        ano_ingresso = str(self.data_de_ingresso.year)
        nome_abreviado = self.nome[:3].upper()
                
        while True:        
            numeros_aleatorios = ''.join(random.choices('0123456789', k=4))
            matricula = ano_ingresso + nome_abreviado + numeros_aleatorios
            if not Aluno.objects.filter(matricula=matricula).exists():
                break
            
        self.matricula = matricula
    
    def validate_cpf(self):
        self.cpf = re.sub(r'\D', '', self.cpf)
        cpf = CPF()
        if not cpf.validate(self.cpf):
            raise ValidationError(f'CPF inválido!')
        

    def save(self, *args, **kwargs):
        if not self.matricula:
            self.gerar_matricula()
        self.validate_cpf()
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos" 




class Disciplina(models.Model):
    instituicao = models.ForeignKey(Empresa, verbose_name='Instituição', on_delete=models.CASCADE, blank=True, null=True)
    nome = models.CharField("Nome da Disciplina", max_length=100)
    descricao = models.TextField("Descrição da Disciplina", blank=True, null=True)
    carga_horaria = models.PositiveIntegerField("Carga Horária")
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, verbose_name="Professor Responsável", blank=True, null=True)
    material_didatico = models.TextField("Material Didático", blank=True, null=True, help_text="Liste os materiais didáticos recomendados")
    ementa = models.TextField("Ementa da Disciplina", blank=True, null=True, help_text="Conteúdo programático da disciplina")
    bibliografia_basica = models.TextField("Bibliografia Básica", blank=True, null=True)
    bibliografia_complementar = models.TextField("Bibliografia Complementar", blank=True, null=True)
    ativo = models.BooleanField("Disciplina Ativa", default=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"
        ordering = ['nome']


class SaladeAula(models.Model):

    NUMERO_ANDAR = (
        ('T', 'Térreo'),
        ('1', '1º Andar'),
        ('2', '2º Andar'),
        ('3', '3º Andar'),
        ('4', '4º Andar'),
        ('5', '5º Andar'),
        ('6', '6º Andar'),
    )
    
    ESTADO_CONSERVACAO = (
        ('O', 'Ótimo'),
        ('B', 'Bom'),
        ('R', 'Regular'),
        ('P', 'Precário'),
    )   
        
    instituicao = models.ForeignKey(Empresa, verbose_name='Instituição', on_delete=models.CASCADE, blank=True, null=True)
    numero = models.CharField("Sala de Aula", max_length=5)
    capacidade = models.IntegerField("Capacidade da Sala")
    andar = models.CharField("Andar", choices=NUMERO_ANDAR, max_length=1)
    recursos_tecnologicos = models.TextField("Recursos Tecnológicos", blank=True, null=True, help_text="Liste os recursos tecnológicos disponíveis (ex: projetor, computador, etc.)")
    recursos_didaticos = models.TextField("Recursos Didáticos", blank=True, null=True, help_text="Liste os recursos didáticos disponíveis (ex: quadro branco, flip chart, etc.)")
    acessibilidade = models.BooleanField("Acessibilidade para PNE", default=False)
    estado_conservacao = models.CharField("Estado de Conservação", choices=ESTADO_CONSERVACAO, max_length=1)
    observacoes = models.TextField("Observações Adicionais", blank=True, null=True, help_text="Informações adicionais sobre a sala")
    foto = models.ImageField("Foto da Sala", upload_to='sala_de_aula/fotos/%Y/%m/%d/', blank=True, null=True)
    data_de_inspecao = models.DateField("Data da Última Inspeção", blank=True, null=True)
    
    def __str__(self):
        return self.numero
    
    class Meta:
        verbose_name = "Sala de Aula"
        verbose_name_plural = "Salas de Aula"

