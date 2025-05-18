from django import forms
from .models import *
class ProductFormModel(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

