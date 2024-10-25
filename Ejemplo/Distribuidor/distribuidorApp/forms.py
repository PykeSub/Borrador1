from django import forms
from distribuidorApp.models import Distribuidores

class FormDistribuidor(forms.ModelForm):
    class meta:
        model = Distribuidores
        fields = '__all__'