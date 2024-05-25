from .models import Empresa
from rest_framework import serializers

class LandingPageEmpresaFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['cnpj', 'nome_diretor', 'telefone', 'cep', 'email']