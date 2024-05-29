from .models import Serie
from django import forms

class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ["serie", "turno"]