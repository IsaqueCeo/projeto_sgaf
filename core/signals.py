from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Empresa
import requests

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
