from django import forms
from .models import Cat


class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = '__all__'
