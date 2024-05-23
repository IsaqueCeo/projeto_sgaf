from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Empresa
from django.dispatch import receiver
import requests

@receiver(pre_save, sender=Empresa)
def preencher_endereco_via_cep(sender, instance, **kwargs):
    if instance.cep:
        url = f"https://viacep.com.br/ws/{instance.cep}/json/"
        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()
            instance.endereco = dados.get("logradouro", "")
            instance.bairro = dados.get("bairro", "")
            instance.cidade = dados.get("localidade", "")
            instance.estado = dados.get("uf", "")
    