from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Empresa, Dadospessoais, Funcionario, Professor, Aluno
import requests
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role

### Preenchimento Automático de dados da Empresa por Viacep

@receiver(pre_save, sender=Empresa)
def preencher_endereco_via_cep(sender, instance, **kwargs):
    if instance.cep and not instance.endereco:
        try:
            url = f"https://viacep.com.br/ws/{instance.cep}/json/"
            response = requests.get(url)
            if response.status_code == 200:
                dados = response.json()
                instance.endereco = dados.get("logradouro", "")
                instance.bairro = dados.get("bairro", "")
                instance.cidade = dados.get("localidade", "")
                instance.estado = dados.get("uf", "")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao obter dados do CEP: {e}")
            
            
### Preenchimento Automático de dados do Aluno por Viacep

@receiver(pre_save, sender=Aluno)
def preencher_endereco_via_cep(sender, instance, **kwargs):
    if instance.cep and not instance.endereco:
        try:
            url = f"https://viacep.com.br/ws/{instance.cep}/json/"
            response = requests.get(url)
            if response.status_code == 200:
                dados = response.json()
                instance.endereco = dados.get("logradouro", "")
                instance.bairro = dados.get("bairro", "")
                instance.cidade = dados.get("localidade", "")
                instance.estado = dados.get("uf", "")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao obter dados do CEP: {e}")           
            
            
### Preenchimento Automático de dados do Professor por Viacep

@receiver(pre_save, sender=Professor)
def preencher_endereco_via_cep(sender, instance, **kwargs):
    if instance.cep and not instance.endereco:
        try:
            url = f"https://viacep.com.br/ws/{instance.cep}/json/"
            response = requests.get(url)
            if response.status_code == 200:
                dados = response.json()
                instance.endereco = dados.get("logradouro", "")
                instance.bairro = dados.get("bairro", "")
                instance.cidade = dados.get("localidade", "")
                instance.estado = dados.get("uf", "")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao obter dados do CEP: {e}")          


### Preenchimento Automático de dados do Professor por Viacep

@receiver(pre_save, sender=Funcionario)
def preencher_endereco_via_cep(sender, instance, **kwargs):
    if instance.cep and not instance.endereco:
        try:
            url = f"https://viacep.com.br/ws/{instance.cep}/json/"
            response = requests.get(url)
            if response.status_code == 200:
                dados = response.json()
                instance.endereco = dados.get("logradouro", "")
                instance.bairro = dados.get("bairro", "")
                instance.cidade = dados.get("localidade", "")
                instance.estado = dados.get("uf", "")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao obter dados do CEP: {e}")         

            
### Preenchimento Automático de dados da Empresa por CNPJ            

@receiver(pre_save, sender=Empresa)
def preencher_dados_pelo_cnpj(sender, instance, **kwargs):
    if instance.cnpj and not instance.razao_social:
        try:
            url = f"https://api.cnpjs.dev/v1/{instance.cnpj}"
            response = requests.get(url)
            if response.status_code == 200:
                dados = response.json()
                instance.razao_social = dados.get("razao_social", "")
                instance.nome_fantasia = dados.get("nome_fantasia", "")
                instance.natureza_juridica = dados.get("natureza_juridica", "")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao obter dados do CNPJ: {e}")


### Criando tabela de dados pessoais do Funcionário

@receiver(post_save, sender=Funcionario)
def criar_dados_pessoais_do_funcionario(sender, instance, created, **kwargs):
    if created:
        dados_funcionario = Dadospessoais.objects.create(
            nome=instance.nome,
            nome_da_mae=instance.nome_da_mae,
            data_nascimento=instance.data_nascimento,
            uf_naturalizado=instance.uf_naturalizado,
            uf=instance.uf,
            cep=instance.cep,
            cidade=instance.cidade,
            endereco=instance.endereco,
            bairro=instance.bairro,
            numero=instance.numero,
            nacionalidade=instance.nacionalidade,
            cpf=instance.cpf,
            rg=instance.rg
        )
        dados_funcionario.save()
        instance.dados_pessoais = dados_funcionario
        instance.save()


### Criando usuário de login do Funcionário 

@receiver(post_save, sender=Funcionario)
def criar_usuario_funcionario(sender, instance, created, **kwargs):
    if created:
        funcionario = User.objects.create(
            username=instance.matricula,              
            email=instance.email, 
            first_name=instance.nome.split()[0],
            last_name=' '.join(instance.nome.split()[1:])
            )
        funcionario.set_password(instance.cpf)
        funcionario.save()
        assign_role(funcionario, 'funcionario')
        instance.usuario = funcionario
        instance.save()
        
### Criando tabela de dados pessoais do Professor      
        
@receiver(post_save, sender=Professor)
def criar_dados_pessoais_do_professor(sender, instance, created, **kwargs):
    if created:
        dados_professor = Dadospessoais.objects.create(
            nome=instance.nome,
            nome_da_mae=instance.nome_da_mae,
            data_nascimento=instance.data_nascimento,
            uf_naturalizado=instance.uf_naturalizado,
            uf=instance.uf,
            cep=instance.cep,
            cidade=instance.cidade,
            endereco=instance.endereco,
            bairro=instance.bairro,
            numero=instance.numero,
            nacionalidade=instance.nacionalidade,
            cpf=instance.cpf,
            rg=instance.rg
        )
        dados_professor.save()
        instance.dados_pessoais = dados_professor
        instance.save()


### Criando usuário de login do Professor 

@receiver(post_save, sender=Professor)
def criar_usuario_professor(sender, instance, created, **kwargs):
    if created:
        usuario_professor = User.objects.create(
            username=instance.matricula,              
            email=instance.email, 
            first_name=instance.nome.split()[0],
            last_name=' '.join(instance.nome.split()[1:])
            )
        usuario_professor.set_password(instance.cpf)
        usuario_professor.save()
        assign_role(usuario_professor, 'professor')
        instance.usuario = usuario_professor
        instance.save()



### Criando tabela de dados pessoais do Aluno     
        
@receiver(post_save, sender=Aluno)
def criar_dados_pessoais_do_aluno(sender, instance, created, **kwargs):
    if created:
        dados_aluno = Dadospessoais.objects.create(
            nome=instance.nome,
            nome_da_mae=instance.nome_da_mae,
            data_nascimento=instance.data_nascimento,
            uf_naturalizado=instance.uf_naturalizado,
            uf=instance.uf,
            cep=instance.cep,
            cidade=instance.cidade,
            endereco=instance.endereco,
            bairro=instance.bairro,
            numero=instance.numero,
            nacionalidade=instance.nacionalidade,
            cpf=instance.cpf,
            rg=instance.rg
        )
        dados_aluno.save()
        instance.dados_pessoais = dados_aluno
        instance.save()


### Criando usuário de login do Aluno 

@receiver(post_save, sender=Aluno)
def criar_usuario_aluno(sender, instance, created, **kwargs):
    if created:
        usuario_aluno = User.objects.create(
            username=instance.matricula,              
            email=instance.email, 
            first_name=instance.nome.split()[0],
            last_name=' '.join(instance.nome.split()[1:])
            )
        usuario_aluno.set_password(instance.cpf)
        usuario_aluno.save()
        assign_role(usuario_aluno, 'aluno')
        instance.usuario = usuario_aluno
        instance.save()