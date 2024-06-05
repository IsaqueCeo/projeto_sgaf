from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a sua matrícula', 'id': 'id_usuario', 'required': True}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite a sua senha', 'id': 'id_senha', 'required': True}))
