from django.test import TestCase
from unittest.mock import patch
from .models import Empresa

class EmpresaModelTest(TestCase):
    @patch('requests.get')
    def test_pre_save_signal(self, mock_get):        
        mock_response = {
        "logradouro": "Praça da Sé",  
        "bairro": "Sé",
        "localidade": "São Paulo",
        "uf": "SP"
}

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        empresa = Empresa(
            razao_social="Empresa Exemplo",
            nome_fantasia="Fantasia Exemplo",
            cnpj="12345678901234",
            email="email@exemplo.com",
            telefone="12345678901",
            cep="01001000",  
        )

        empresa.save()


        self.assertEqual(empresa.endereco, "Praça da Sé")
        self.assertEqual(empresa.bairro, "Sé")
        self.assertEqual(empresa.cidade, "São Paulo")
        self.assertEqual(empresa.estado, "SP")
